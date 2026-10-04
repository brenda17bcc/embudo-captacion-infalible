import re
import streamlit as st
from database import crear_tabla, guardar_contacto, guardar_candidato

# ---------- CONFIGURACIÓN ----------
st.set_page_config(
    page_title="Embudo de Captación Infalible",
    page_icon="💡",
    layout="centered"
)
crear_tabla()

SERVICIOS = [
    "🏥 Seguro médico",
    "🦷 Seguro dental",
    "🚗 Seguro de coche",
    "💡 Luz",
    "🌐 Internet",
    "📺 TV / Cable",
    "📱 Móvil",
    "🏠 Hipoteca",
]


# ---------- FUNCIONES AUXILIARES ----------
def validar_datos(nombre, telefono, email, acepta):
    """Revisa los datos comunes. Devuelve la lista de errores y el teléfono limpio."""
    errores = []

    if not nombre.strip():
        errores.append("Escribe tu nombre.")

    telefono_limpio = re.sub(r"[\s\-]", "", telefono)
    if not re.fullmatch(r"\+?\d{9,15}", telefono_limpio):
        errores.append("Escribe un teléfono válido (mínimo 9 dígitos).")

    if email.strip() and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
        errores.append("El email no parece válido.")

    if not acepta:
        errores.append("Debes aceptar el uso de tus datos para que podamos contactarte.")

    return errores, telefono_limpio


def primer_nombre(nombre_completo):
    """De 'maria lopez garcia' devuelve 'Maria', para un trato más cercano."""
    partes = nombre_completo.strip().split()
    return partes[0].capitalize() if partes else ""


# ---------- VENTANA EMERGENTE: ÚNETE AL EQUIPO ----------
@st.dialog("🤝 Únete al equipo")
def dialogo_equipo():
    st.write(
        "¿Te gustaría **generar ingresos** ayudando a otras personas a ahorrar? "
        "Déjanos tus datos y te contamos cómo funciona, sin compromiso."
    )

    with st.form("formulario_equipo"):
        e_nombre = st.text_input("Nombre *", key="e_nombre")
        e_telefono = st.text_input("Teléfono / WhatsApp *", key="e_telefono")
        e_email = st.text_input("Email (opcional)", key="e_email")
        e_ciudad = st.text_input("Ciudad", key="e_ciudad")
        e_situacion = st.selectbox(
            "¿Cuál es tu situación actual?",
            ["Busco empleo", "Quiero ingresos extra",
             "Ya trabajo como autónomo/a", "Otra"],
            key="e_situacion"
        )
        e_experiencia = st.selectbox(
            "¿Tienes experiencia en ventas o atención al cliente?",
            ["Ninguna", "Ventas / comercial", "Seguros",
             "Energía o telecomunicaciones", "Otra"],
            key="e_experiencia"
        )
        e_disponibilidad = st.selectbox(
            "¿Qué disponibilidad tienes?",
            ["Tiempo completo", "Media jornada", "Solo algunas horas"],
            key="e_disponibilidad"
        )
        e_mensaje = st.text_area("¿Algo que quieras contarnos? (opcional)", key="e_mensaje")
        e_acepta = st.checkbox(
            "Acepto que mis datos se usen para contactarme sobre esta oportunidad *",
            key="e_acepta"
        )
        e_enviado = st.form_submit_button("🚀 Quiero más información")

    if e_enviado:
        errores, telefono_limpio = validar_datos(e_nombre, e_telefono, e_email, e_acepta)
        if errores:
            for error in errores:
                st.error(error)
        else:
            guardar_candidato(
                nombre=e_nombre.strip(),
                telefono=telefono_limpio,
                email=e_email.strip(),
                ciudad=e_ciudad.strip(),
                situacion=e_situacion,
                experiencia=e_experiencia,
                disponibilidad=e_disponibilidad,
                mensaje=e_mensaje.strip(),
                consentimiento=e_acepta,
            )
            st.success(
                f"¡Gracias, {primer_nombre(e_nombre)}! 🙌 "
                "Te contactaremos pronto para contarte más."
            )


# ---------- CABECERA ----------
st.title("💡 ¿Estás pagando de más?")
st.subheader("Compara y ahorra en tus servicios del hogar")
st.write(
    "Déjanos tus datos y un asesor te preparará una propuesta "
    "**gratis y sin compromiso**."
)

# ---------- BARRA DE PROGRESO ----------
# Calculamos en qué punto del embudo está la persona
seleccion_actual = st.session_state.get("servicios", [])
if not seleccion_actual:
    avance, etiqueta = 0.10, "Paso 1 de 3 · Elige tus servicios"
elif not st.session_state.get("contacto_enviado", False):
    avance, etiqueta = 0.55, "Paso 2 de 3 · Cuéntanos cuánto pagas"
else:
    avance, etiqueta = 1.0, "¡Completado! 🎉"

st.progress(avance, text=etiqueta)

# ---------- PASO 1: SERVICIOS ----------
st.markdown("### 1️⃣ ¿En qué te gustaría ahorrar?")
seleccion = st.multiselect("Elige uno o varios servicios", SERVICIOS, key="servicios")

if not seleccion:
    st.info("👆 Elige al menos un servicio para continuar.")
else:
    # ---------- PASO 2: GASTO ACTUAL ----------
    st.markdown("### 2️⃣ ¿Cuánto pagas ahora al mes?")
    st.caption("Un valor aproximado es suficiente. Si no lo sabes, déjalo en 0.")

    pagos = {}
    for servicio in seleccion:
        pagos[servicio] = st.number_input(
            f"{servicio} (€/mes)",
            min_value=0.0,
            step=5.0,
            key=f"pago_{servicio}"
        )

    total_mensual = sum(pagos.values())
    if total_mensual > 0:
        col1, col2 = st.columns(2)
        col1.metric("Pagas al mes", f"{total_mensual:,.0f} €")
        col2.metric("Pagas al año", f"{total_mensual * 12:,.0f} €")
        st.caption("Veamos cuánto de esto podemos reducir. 👇")

    # ---------- PASO 3: CONTACTO ----------
    st.markdown("### 3️⃣ ¿Dónde te enviamos tu propuesta?")
    with st.form("formulario_contacto"):
        nombre = st.text_input("Nombre *", key="c_nombre")
        telefono = st.text_input("Teléfono / WhatsApp *", key="c_telefono")
        email = st.text_input("Email (opcional)", key="c_email")
        ciudad = st.text_input("Ciudad o código postal", key="c_ciudad")
        horario = st.selectbox(
            "¿Cuándo prefieres que te contactemos?",
            ["Indiferente", "Mañana", "Tarde"],
            key="c_horario"
        )
        acepta = st.checkbox(
            "Acepto que mis datos se usen para contactarme "
            "con una propuesta personalizada *",
            key="c_acepta"
        )
        enviado = st.form_submit_button("💰 Quiero mi propuesta gratis")

    if enviado:
        errores, telefono_limpio = validar_datos(nombre, telefono, email, acepta)
        if errores:
            for error in errores:
                st.error(error)
        else:
            guardar_contacto(
                nombre=nombre.strip(),
                telefono=telefono_limpio,
                email=email.strip(),
                ciudad=ciudad.strip(),
                horario=horario,
                pagos=pagos,
                consentimiento=acepta,
            )
            # Recordamos que ya envió, para mostrarle la oferta del equipo
            st.session_state["contacto_enviado"] = True
            st.session_state["nombre_cliente"] = primer_nombre(nombre)
            st.balloons()

# ---------- DESPUÉS DE ENVIAR: EL MOMENTO DE ORO ----------
if st.session_state.get("contacto_enviado", False):
    st.success(
        f"¡Gracias, {st.session_state['nombre_cliente']}! 🎉 "
        "Un asesor te contactará pronto con tu propuesta."
    )

    st.markdown("---")
    st.markdown("#### 💼 Una última cosa...")
    st.write(
        "Mucha gente que empieza ahorrando acaba **ayudando a otros a ahorrar** "
        "y generando ingresos con ello. ¿Te lo contamos?"
    )
    if st.button("🤝 Sí, cuéntame cómo", key="btn_equipo_final"):
        dialogo_equipo()

# ---------- PIE DE PÁGINA: ACCESO DISCRETO ----------
st.markdown("---")
st.caption("¿Buscas una oportunidad profesional en lugar de ahorrar?")
if st.button("🤝 Únete al equipo", key="btn_equipo_pie"):
    dialogo_equipo()