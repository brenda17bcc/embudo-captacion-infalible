"""Embudo de Captación Infalible — aplicación principal.

Tres embudos en una sola página:
  1. Ahorro en servicios del hogar (seguros, luz, internet, móvil, hipoteca).
  2. Compra, venta y alquiler de vivienda.
  3. Captación de personas para el equipo (ventana emergente).
Disponible en 7 idiomas.
"""

import base64
import os
import re
import urllib.parse

import streamlit as st

import config
from estilos import obtener_paleta, css
from database import (crear_tabla, guardar_contacto, guardar_candidato,
                      guardar_inmueble)
from idiomas import IDIOMAS, PREFIJOS, CLAVES_SERVICIOS, SERVICIOS, t, servicios
from idiomas_inmo import ti

# ---------- CONFIGURACIÓN ----------
st.set_page_config(
    page_title=f"{config.MARCA} · Embudo de Captación",
    page_icon="🏡",
    layout="centered",
)
crear_tabla()

paleta = obtener_paleta(config.PALETA)


def archivo_en_base64(ruta):
    """Convierte una imagen en texto para poder incrustarla en el HTML."""
    if not ruta or not os.path.exists(ruta):
        return None
    with open(ruta, "rb") as archivo:
        return base64.b64encode(archivo.read()).decode()


# El icono del logo se usa como marca de agua muy suave de fondo
st.markdown(css(paleta, archivo_en_base64(config.ICONO)), unsafe_allow_html=True)

# Barra fija superior: el logo siempre visible, aunque se baje por la página
_ruta_logo = config.LOGO_CLARO if paleta.get("logo_claro") else config.LOGO
_logo_barra = archivo_en_base64(_ruta_logo)
if _logo_barra:
    st.markdown(
        f'<div class="barra-marca">'
        f'<img src="data:image/png;base64,{_logo_barra}" alt="{config.MARCA}">'
        f'</div>',
        unsafe_allow_html=True,
    )


# ---------- FUNCIONES AUXILIARES ----------
def validar_datos(idioma, nombre, numero, email, acepta):
    """Revisa los datos comunes. Devuelve los errores y el número limpio."""
    errores = []

    if not nombre.strip():
        errores.append(t(idioma, "err_nombre"))

    numero_limpio = re.sub(r"[\s\-\.]", "", numero)
    if not re.fullmatch(r"\d{6,14}", numero_limpio):
        errores.append(t(idioma, "err_telefono"))

    if email.strip() and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
        errores.append(t(idioma, "err_email"))

    if not acepta:
        errores.append(t(idioma, "err_consent"))

    return errores, numero_limpio


def primer_nombre(nombre_completo):
    """De 'maria lopez garcia' devuelve 'Maria', para un trato más cercano."""
    partes = nombre_completo.strip().split()
    return partes[0].capitalize() if partes else ""


def telefono_completo(prefijo, numero):
    """Une el prefijo del país con el número: '+34 612345678'."""
    return f"{prefijo.split()[-1]} {numero}"


def enlace_whatsapp(idioma):
    """Crea el enlace de WhatsApp con un mensaje ya escrito."""
    mensaje = urllib.parse.quote(t(idioma, "wa_mensaje"))
    return f"https://wa.me/{config.WHATSAPP}?text={mensaje}"


def mostrar_logo(ancho=220):
    """Muestra el logo completo. En fondos oscuros usa la versión clara."""
    ruta = config.LOGO_CLARO if paleta.get("logo_claro") else config.LOGO
    if os.path.exists(ruta):
        st.image(ruta, width=ancho)


def mostrar_foto(tam=140):
    """Muestra la foto del asesor en redondo. Si no hay foto, pone un icono."""
    imagen = archivo_en_base64(config.FOTO)
    if imagen:
        st.markdown(
            f'<img class="foto-asesor" width="{tam}" '
            f'src="data:image/png;base64,{imagen}" alt="{config.NOMBRE}">',
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="avatar">👤</div>', unsafe_allow_html=True)


# ---------- VENTANA EMERGENTE: ÚNETE AL EQUIPO ----------
def abrir_dialogo_equipo(idioma):
    """Abre la ventana emergente de captación de equipo, en el idioma elegido."""

    @st.dialog(t(idioma, "equipo_titulo"))
    def _dialogo():
        st.write(t(idioma, "equipo_intro"))

        with st.form("formulario_equipo"):
            e_nombre = st.text_input(t(idioma, "nombre"), key="e_nombre")

            col_pref, col_tel = st.columns([1, 2])
            e_prefijo = col_pref.selectbox(t(idioma, "prefijo"), PREFIJOS, key="e_prefijo")
            e_numero = col_tel.text_input(t(idioma, "telefono"), key="e_numero")

            e_email = st.text_input(t(idioma, "email"), key="e_email")
            e_ciudad = st.text_input(t(idioma, "equipo_ciudad"), key="e_ciudad")
            e_situacion = st.selectbox(
                t(idioma, "equipo_situacion"), t(idioma, "situacion_opts"),
                key="e_situacion"
            )
            e_experiencia = st.selectbox(
                t(idioma, "equipo_experiencia"), t(idioma, "experiencia_opts"),
                key="e_experiencia"
            )
            e_disponibilidad = st.selectbox(
                t(idioma, "equipo_disponibilidad"), t(idioma, "disponibilidad_opts"),
                key="e_disponibilidad"
            )
            e_mensaje = st.text_area(t(idioma, "equipo_mensaje"), key="e_mensaje")
            e_acepta = st.checkbox(t(idioma, "equipo_consent"), key="e_acepta")
            e_enviado = st.form_submit_button(t(idioma, "equipo_boton"))

        if e_enviado:
            errores, numero_limpio = validar_datos(
                idioma, e_nombre, e_numero, e_email, e_acepta
            )
            if errores:
                for error in errores:
                    st.error(error)
            else:
                guardar_candidato(
                    nombre=e_nombre.strip(),
                    telefono=telefono_completo(e_prefijo, numero_limpio),
                    email=e_email.strip(),
                    ciudad=e_ciudad.strip(),
                    situacion=e_situacion,
                    experiencia=e_experiencia,
                    disponibilidad=e_disponibilidad,
                    mensaje=e_mensaje.strip(),
                    consentimiento=e_acepta,
                    idioma=idioma,
                )
                st.success(
                    t(idioma, "equipo_gracias").format(nombre=primer_nombre(e_nombre))
                )

    _dialogo()


# ---------- SELECTOR DE IDIOMA ----------
col_vacio_top, col_idioma = st.columns([3, 2])
with col_idioma:
    idioma_elegido = st.selectbox(
        "🌍", list(IDIOMAS.keys()), key="idioma_nombre", label_visibility="collapsed"
    )
idioma = IDIOMAS[idioma_elegido]

# Al cambiar de idioma limpiamos lo elegido: estaba guardado en el idioma anterior
if st.session_state.get("idioma_actual") != idioma:
    st.session_state["idioma_actual"] = idioma
    st.session_state["servicios"] = []
    st.session_state.pop("modo", None)

# ---------- CABECERA (cambia según el embudo elegido) ----------
OPCIONES_MODO = [ti(idioma, "modo_ahorro"), ti(idioma, "modo_inmo")]
modo_actual = st.session_state.get("modo") or OPCIONES_MODO[0]
es_vivienda = modo_actual == OPCIONES_MODO[1]

if es_vivienda:
    st.title(ti(idioma, "inmo_titulo"))
    st.write(ti(idioma, "inmo_intro"))
else:
    st.title(t(idioma, "titulo"))
    st.subheader(t(idioma, "subtitulo"))
    st.write(t(idioma, "intro"))

# ---------- TARJETA DEL ASESOR ----------
col_foto, col_datos = st.columns([1, 3])

with col_foto:
    mostrar_foto()

with col_datos:
    frases = config.CLAIM_INMO if es_vivienda else config.CLAIM
    claim = frases.get(idioma, frases["es"])
    st.markdown(
        f'<p class="asesor-nombre">{config.NOMBRE}</p>'
        f'<p class="asesor-claim">{claim}</p>'
        f'<p class="asesor-claim">'
        f'{ti(idioma, "ambito") if es_vivienda else "📍 " + config.ZONA}</p>',
        unsafe_allow_html=True,
    )
    st.link_button(t(idioma, "whatsapp_boton"), enlace_whatsapp(idioma))

# ---------- SELLOS DE CONFIANZA ----------
st.markdown(
    f'<div>'
    f'<span class="sello">{t(idioma, "sello_seguridad")}</span>'
    f'<span class="sello">{t(idioma, "sello_gratis")}</span>'
    f'<span class="sello">{t(idioma, "sello_persona")}</span>'
    f'</div>',
    unsafe_allow_html=True,
)

st.markdown("")

# ---------- ELEGIR EMBUDO: AHORRO O VIVIENDA ----------
if hasattr(st, "segmented_control"):
    modo = st.segmented_control(
        ti(idioma, "modo_pregunta"), OPCIONES_MODO,
        default=OPCIONES_MODO[0], key="modo"
    )
else:
    modo = st.radio(
        ti(idioma, "modo_pregunta"), OPCIONES_MODO, horizontal=True, key="modo"
    )

if modo is None:
    modo = OPCIONES_MODO[0]

# =====================================================
# EMBUDO 1: AHORRO EN SERVICIOS
# =====================================================
if modo == OPCIONES_MODO[0]:

    # ---------- CÓMO FUNCIONA ----------
    st.markdown(f"### {t(idioma, 'como_funciona')}")
    col_a, col_b, col_c = st.columns(3)
    for columna, titulo_clave, texto_clave in [
        (col_a, "paso_a_t", "paso_a_d"),
        (col_b, "paso_b_t", "paso_b_d"),
        (col_c, "paso_c_t", "paso_c_d"),
    ]:
        columna.markdown(
            f'<div class="tarjeta"><h4>{t(idioma, titulo_clave)}</h4>'
            f'<p>{t(idioma, texto_clave)}</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown("")

    # ---------- BARRA DE PROGRESO ----------
    if not st.session_state.get("servicios", []):
        avance, etiqueta = 0.10, t(idioma, "prog1")
    elif not st.session_state.get("contacto_enviado", False):
        avance, etiqueta = 0.55, t(idioma, "prog2")
    else:
        avance, etiqueta = 1.0, t(idioma, "prog3")

    st.progress(avance, text=etiqueta)

    # ---------- PASO 1: SERVICIOS ----------
    st.markdown(f"### {t(idioma, 'paso1_titulo')}")

    opciones = servicios(idioma)
    traducciones = SERVICIOS.get(idioma, SERVICIOS["es"])
    etiqueta_a_clave = {traducciones[clave]: clave for clave in CLAVES_SERVICIOS}

    seleccion = st.multiselect(
        t(idioma, "elige"), opciones, key="servicios",
        placeholder=t(idioma, "placeholder")
    )

    if not seleccion:
        st.info(t(idioma, "aviso_elige"))
    else:
        # ---------- PASO 2: GASTO ACTUAL ----------
        st.markdown(f"### {t(idioma, 'paso2_titulo')}")
        st.caption(t(idioma, "aprox"))

        pagos = {}
        for etiqueta_visible in seleccion:
            clave = etiqueta_a_clave[etiqueta_visible]
            nombre_es = SERVICIOS["es"][clave]
            pagos[nombre_es] = st.number_input(
                f"{etiqueta_visible} (€/mes)",
                min_value=0.0, step=5.0, key=f"pago_{clave}"
            )

        total_mensual = sum(pagos.values())
        if total_mensual > 0:
            col1, col2 = st.columns(2)
            col1.metric(t(idioma, "pagas_mes"), f"{total_mensual:,.0f} €")
            col2.metric(t(idioma, "pagas_anio"), f"{total_mensual * 12:,.0f} €")
            st.caption(t(idioma, "veamos"))

        # ---------- PASO 3: CONTACTO ----------
        st.markdown(f"### {t(idioma, 'paso3_titulo')}")
        with st.form("formulario_contacto"):
            nombre = st.text_input(t(idioma, "nombre"), key="c_nombre")

            col_pref, col_tel = st.columns([1, 2])
            prefijo = col_pref.selectbox(t(idioma, "prefijo"), PREFIJOS, key="c_prefijo")
            numero = col_tel.text_input(t(idioma, "telefono"), key="c_numero")

            email = st.text_input(t(idioma, "email"), key="c_email")
            ciudad = st.text_input(t(idioma, "ciudad"), key="c_ciudad")
            horario = st.selectbox(
                t(idioma, "horario"), t(idioma, "horario_opts"), key="c_horario"
            )
            acepta = st.checkbox(t(idioma, "consent"), key="c_acepta")
            enviado = st.form_submit_button(t(idioma, "boton_enviar"))

        if enviado:
            errores, numero_limpio = validar_datos(idioma, nombre, numero, email, acepta)
            if errores:
                for error in errores:
                    st.error(error)
            else:
                guardar_contacto(
                    nombre=nombre.strip(),
                    telefono=telefono_completo(prefijo, numero_limpio),
                    email=email.strip(),
                    ciudad=ciudad.strip(),
                    horario=horario,
                    pagos=pagos,
                    consentimiento=acepta,
                    idioma=idioma,
                )
                st.session_state["contacto_enviado"] = True
                st.session_state["nombre_cliente"] = primer_nombre(nombre)
                st.balloons()

    # ---------- DESPUÉS DE ENVIAR: EL MOMENTO DE ORO ----------
    if st.session_state.get("contacto_enviado", False):
        st.success(
            t(idioma, "gracias").format(nombre=st.session_state["nombre_cliente"])
        )

        st.markdown("---")
        st.markdown(f"#### {t(idioma, 'cierre_titulo')}")
        st.write(t(idioma, "cierre_texto"))
        if st.button(t(idioma, "cierre_boton"), key="btn_equipo_final"):
            abrir_dialogo_equipo(idioma)

# =====================================================
# EMBUDO 2: VIVIENDA — COMPRA, VENTA, ALQUILER Y COLABORACIÓN
# =====================================================
else:
    st.markdown(
        f'<span class="sello">{ti(idioma, "inmo_sello")}</span>'
        f'<span class="sello">{ti(idioma, "inmo_sello_alq")}</span>',
        unsafe_allow_html=True,
    )

    # ---------- PASO 1: LA OPERACIÓN ----------
    st.markdown(f"### {ti(idioma, 'inmo_paso1')}")

    operaciones = ti(idioma, "operacion_opts")
    operacion = st.selectbox(ti(idioma, "operacion"), operaciones, key="i_operacion")
    # 0 comprar · 1 vender · 2 busco alquiler · 3 alquilo mi piso · 4 agente
    caso = operaciones.index(operacion)

    detalles = {}
    zona, tipo, plazo, financiacion = "", "", "", ""
    habitaciones, importe = 0, 0.0

    if caso in (0, 1):
        # ---- COMPRAR O VENDER ----
        col_tipo, col_hab = st.columns([2, 1])
        tipo = col_tipo.selectbox(ti(idioma, "tipo"), ti(idioma, "tipo_opts"),
                                  key="i_tipo")
        habitaciones = col_hab.number_input(ti(idioma, "habitaciones"),
                                            min_value=0, max_value=15, step=1,
                                            key="i_hab")
        zona = st.text_input(ti(idioma, "zona"), key="i_zona")
        etiqueta_importe = (ti(idioma, "importe_venta") if caso == 1
                            else ti(idioma, "importe_compra"))
        importe = st.number_input(etiqueta_importe, min_value=0, step=5000,
                                  key="i_importe")
        col_plazo, col_fin = st.columns(2)
        plazo = col_plazo.selectbox(ti(idioma, "plazo"), ti(idioma, "plazo_opts"),
                                    key="i_plazo")
        financiacion = col_fin.selectbox(ti(idioma, "financiacion"),
                                         ti(idioma, "financiacion_opts"),
                                         key="i_fin")

    elif caso == 2:
        # ---- BUSCO PISO DE ALQUILER ----
        col_tipo, col_hab = st.columns([2, 1])
        tipo = col_tipo.selectbox(ti(idioma, "tipo"), ti(idioma, "tipo_opts"),
                                  key="i_tipo_alq")
        habitaciones = col_hab.number_input(ti(idioma, "habitaciones"),
                                            min_value=0, max_value=10, step=1,
                                            key="i_hab_alq")
        zona = st.text_input(ti(idioma, "zona"), key="i_zona_alq")

        col_pres, col_dur = st.columns(2)
        importe = col_pres.number_input(ti(idioma, "alq_presupuesto"),
                                        min_value=0, step=50, key="i_presupuesto")
        plazo = col_dur.selectbox(ti(idioma, "alq_duracion"),
                                  ti(idioma, "alq_duracion_opts"), key="i_duracion")
        detalles["duracion"] = plazo

        col_ent, col_per = st.columns(2)
        entrada = col_ent.date_input(ti(idioma, "alq_entrada"), key="i_entrada")
        detalles["entrada"] = str(entrada)
        detalles["personas"] = int(
            col_per.number_input(ti(idioma, "alq_personas"), min_value=1,
                                 max_value=12, step=1, key="i_personas")
        )

        col_mas, col_sit = st.columns(2)
        detalles["mascotas"] = col_mas.selectbox(
            ti(idioma, "alq_mascotas"), ti(idioma, "alq_mascotas_opts"),
            key="i_mascotas"
        )
        detalles["situacion_laboral"] = col_sit.selectbox(
            ti(idioma, "alq_situacion"), ti(idioma, "alq_situacion_opts"),
            key="i_situacion"
        )
        detalles["acredita_ingresos"] = st.selectbox(
            ti(idioma, "alq_acredita"), ti(idioma, "alq_acredita_opts"),
            key="i_acredita"
        )

    elif caso == 3:
        # ---- QUIERO ALQUILAR MI PISO (PROPIETARIO) ----
        col_tipo, col_hab = st.columns([2, 1])
        tipo = col_tipo.selectbox(ti(idioma, "tipo"), ti(idioma, "tipo_opts"),
                                  key="i_tipo_prop")
        habitaciones = col_hab.number_input(ti(idioma, "habitaciones"),
                                            min_value=0, max_value=15, step=1,
                                            key="i_hab_prop")
        zona = st.text_input(ti(idioma, "zona"), key="i_zona_prop")

        col_renta, col_amu = st.columns(2)
        importe = col_renta.number_input(ti(idioma, "prop_renta"),
                                         min_value=0, step=50, key="i_renta")
        detalles["amueblado"] = col_amu.selectbox(
            ti(idioma, "prop_amueblado"), ti(idioma, "prop_amueblado_opts"),
            key="i_amueblado"
        )

        col_disp, col_mas = st.columns(2)
        disponible = col_disp.date_input(ti(idioma, "prop_disponible"),
                                         key="i_disponible")
        detalles["disponible_desde"] = str(disponible)
        detalles["admite_mascotas"] = col_mas.selectbox(
            ti(idioma, "prop_mascotas"), ti(idioma, "prop_mascotas_opts"),
            key="i_admite_mascotas"
        )
        plazo = st.selectbox(ti(idioma, "prop_gestion"),
                             ti(idioma, "prop_gestion_opts"), key="i_gestion")
        detalles["gestion"] = plazo

    else:
        # ---- SOY AGENTE Y QUIERO COLABORAR ----
        detalles["agencia"] = st.text_input(ti(idioma, "col_agencia"),
                                            key="i_agencia")
        zona = st.text_input(ti(idioma, "col_zona"), key="i_zona_col")
        detalles["tipo_colaboracion"] = st.selectbox(
            ti(idioma, "col_tipo"), ti(idioma, "col_tipo_opts"), key="i_col_tipo"
        )
        detalles["cartera"] = int(
            st.number_input(ti(idioma, "col_cartera"), min_value=0, max_value=500,
                            step=1, key="i_cartera")
        )
        detalles["nota"] = st.text_area(ti(idioma, "col_nota"), key="i_col_nota")
        tipo = "—"
        plazo = detalles["tipo_colaboracion"]

    # ---------- PASO 2: CONTACTO ----------
    st.markdown(f"### {ti(idioma, 'inmo_paso2')}")
    with st.form("formulario_inmueble"):
        i_nombre = st.text_input(t(idioma, "nombre"), key="i_nombre")
        i_residencia = st.text_input(ti(idioma, "residencia"), key="i_residencia")

        col_pref_i, col_tel_i = st.columns([1, 2])
        i_prefijo = col_pref_i.selectbox(t(idioma, "prefijo"), PREFIJOS,
                                         key="i_prefijo")
        i_numero = col_tel_i.text_input(t(idioma, "telefono"), key="i_numero")

        i_email = st.text_input(t(idioma, "email"), key="i_email")
        i_acepta = st.checkbox(t(idioma, "consent"), key="i_acepta")
        texto_boton = ti(idioma, "col_boton") if caso == 4 else ti(idioma, "inmo_boton")
        i_enviado = st.form_submit_button(texto_boton)

    if i_enviado:
        errores, numero_limpio = validar_datos(
            idioma, i_nombre, i_numero, i_email, i_acepta
        )
        if errores:
            for error in errores:
                st.error(error)
        else:
            detalles["pais_contacto"] = i_residencia.strip()
            guardar_inmueble(
                nombre=i_nombre.strip(),
                telefono=telefono_completo(i_prefijo, numero_limpio),
                email=i_email.strip(),
                zona=zona.strip(),
                operacion=operacion,
                tipo=tipo,
                habitaciones=int(habitaciones),
                importe=float(importe),
                plazo=plazo,
                financiacion=financiacion,
                consentimiento=i_acepta,
                idioma=idioma,
                detalles=detalles,
            )
            mensaje = ti(idioma, "col_gracias") if caso == 4 else ti(idioma, "inmo_gracias")
            st.success(mensaje.format(nombre=primer_nombre(i_nombre)))
            st.balloons()

# ---------- CONTACTO DIRECTO ----------
st.markdown("---")
st.markdown(f"**{t(idioma, 'contacto_directo')}**")
col_wa, col_mail = st.columns(2)
with col_wa:
    st.link_button(t(idioma, "whatsapp_boton"), enlace_whatsapp(idioma))
with col_mail:
    st.link_button(f"✉️ {config.EMAIL}", f"mailto:{config.EMAIL}")

# ---------- PRIVACIDAD ----------
with st.expander(t(idioma, "privacidad_titulo")):
    st.markdown(
        t(idioma, "privacidad_texto").format(
            responsable=f"{config.NOMBRE} — {config.MARCA}",
            email=config.EMAIL_PRIVACIDAD,
        )
    )
    st.caption(
        ti(idioma, "privacidad_identificacion").format(email=config.EMAIL_PRIVACIDAD)
    )

# ---------- PIE DE PÁGINA ----------
st.caption(t(idioma, "pie_texto"))
if st.button(t(idioma, "pie_boton"), key="btn_equipo_pie"):
    abrir_dialogo_equipo(idioma)

st.markdown("<div style='margin-top:2rem'></div>", unsafe_allow_html=True)
col_p1, col_p2, col_p3 = st.columns([1, 2, 1])
with col_p2:
    mostrar_logo(220)
st.markdown(
    f'<p style="text-align:center;color:{paleta["suave"]};font-size:.8rem;'
    f'margin-top:.5rem;">© {config.MARCA} · {config.NOMBRE}</p>',
    unsafe_allow_html=True,
)
