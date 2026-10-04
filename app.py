import re
import streamlit as st
from database import crear_tabla, guardar_contacto, guardar_candidato
from idiomas import IDIOMAS, PREFIJOS, CLAVES_SERVICIOS, SERVICIOS, t, servicios

# ---------- CONFIGURACIÓN ----------
st.set_page_config(
    page_title="Embudo de Captación Infalible",
    page_icon="💡",
    layout="centered"
)
crear_tabla()


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
                t(idioma, "equipo_situacion"), t(idioma, "situacion_opts"), key="e_situacion"
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
col_izq, col_idioma = st.columns([2, 1])
with col_idioma:
    idioma_elegido = st.selectbox(
        "🌍", list(IDIOMAS.keys()), key="idioma_nombre", label_visibility="collapsed"
    )
idioma = IDIOMAS[idioma_elegido]

# Si cambia el idioma, limpiamos los servicios elegidos
if st.session_state.get("idioma_actual") != idioma:
    st.session_state["idioma_actual"] = idioma
    st.session_state["servicios"] = []

# ---------- CABECERA ----------
st.title(t(idioma, "titulo"))
st.subheader(t(idioma, "subtitulo"))
st.write(t(idioma, "intro"))

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
            min_value=0.0,
            step=5.0,
            key=f"pago_{clave}"
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

# ---------- DESPUÉS DE ENVIAR ----------
if st.session_state.get("contacto_enviado", False):
    st.success(t(idioma, "gracias").format(nombre=st.session_state["nombre_cliente"]))

    st.markdown("---")
    st.markdown(f"#### {t(idioma, 'cierre_titulo')}")
    st.write(t(idioma, "cierre_texto"))
    if st.button(t(idioma, "cierre_boton"), key="btn_equipo_final"):
        abrir_dialogo_equipo(idioma)

# ---------- PIE DE PÁGINA ----------
st.markdown("---")
st.caption(t(idioma, "pie_texto"))
if st.button(t(idioma, "pie_boton"), key="btn_equipo_pie"):
    abrir_dialogo_equipo(idioma)
