"""Textos de la app en varios idiomas (internacionalización)."""

# Idiomas disponibles: lo que ve el usuario -> código interno
IDIOMAS = {
    "🇪🇸 Castellano": "es",
    "🇬🇧 English": "en",
}

# Prefijos telefónicos de los países donde capta el cliente
PREFIJOS = [
    "🇪🇸 +34", "🇫🇷 +33", "🇵🇹 +351", "🇮🇹 +39", "🇩🇪 +49",
    "🇬🇧 +44", "🇨🇭 +41", "🇧🇪 +32", "🇳🇱 +31", "🇦🇩 +376",
    "🇮🇪 +353", "🇦🇹 +43", "🇷🇴 +40", "🇲🇦 +212", "🇺🇸 +1",
]

# Orden en que se muestran los servicios
CLAVES_SERVICIOS = [
    "medico", "dental", "coche", "luz",
    "internet", "tv", "movil", "hipoteca",
]

# Nombre de cada servicio en cada idioma
SERVICIOS = {
    "es": {
        "medico": "🏥 Seguro médico",
        "dental": "🦷 Seguro dental",
        "coche": "🚗 Seguro de coche",
        "luz": "💡 Luz",
        "internet": "🌐 Internet",
        "tv": "📺 TV / Cable",
        "movil": "📱 Móvil",
        "hipoteca": "🏠 Hipoteca",
    },
    "en": {
        "medico": "🏥 Health insurance",
        "dental": "🦷 Dental insurance",
        "coche": "🚗 Car insurance",
        "luz": "💡 Electricity",
        "internet": "🌐 Internet",
        "tv": "📺 TV / Cable",
        "movil": "📱 Mobile",
        "hipoteca": "🏠 Mortgage",
    },
}

# Todos los textos de la app
TEXTOS = {
    "es": {
        "idioma_label": "🌍 Idioma",
        "titulo": "💡 ¿Estás pagando de más?",
        "subtitulo": "Compara y ahorra en tus servicios del hogar",
        "intro": "Déjanos tus datos y un asesor te preparará una propuesta "
                 "**gratis y sin compromiso**.",
        "prog1": "Paso 1 de 3 · Elige tus servicios",
        "prog2": "Paso 2 de 3 · Cuéntanos cuánto pagas",
        "prog3": "¡Completado! 🎉",
        "paso1_titulo": "1️⃣ ¿En qué te gustaría ahorrar?",
        "elige": "Elige uno o varios servicios",
        "aviso_elige": "👆 Elige al menos un servicio para continuar.",
        "paso2_titulo": "2️⃣ ¿Cuánto pagas ahora al mes?",
        "aprox": "Un valor aproximado es suficiente. Si no lo sabes, déjalo en 0.",
        "pagas_mes": "Pagas al mes",
        "pagas_anio": "Pagas al año",
        "veamos": "Veamos cuánto de esto podemos reducir. 👇",
        "paso3_titulo": "3️⃣ ¿Dónde te enviamos tu propuesta?",
        "nombre": "Nombre *",
        "prefijo": "Prefijo",
        "telefono": "Teléfono / WhatsApp *",
        "email": "Email (opcional)",
        "ciudad": "Ciudad o código postal",
        "horario": "¿Cuándo prefieres que te contactemos?",
        "horario_opts": ["Indiferente", "Mañana", "Tarde"],
        "consent": "Acepto que mis datos se usen para contactarme "
                   "con una propuesta personalizada *",
        "boton_enviar": "💰 Quiero mi propuesta gratis",
        "err_nombre": "Escribe tu nombre.",
        "err_telefono": "Escribe un teléfono válido (entre 6 y 14 dígitos).",
        "err_email": "El email no parece válido.",
        "err_consent": "Debes aceptar el uso de tus datos para que podamos contactarte.",
        "gracias": "¡Gracias, {nombre}! 🎉 Un asesor te contactará pronto "
                   "con tu propuesta.",
        "cierre_titulo": "💼 Una última cosa...",
        "cierre_texto": "Mucha gente que empieza ahorrando acaba **ayudando a otros "
                        "a ahorrar** y generando ingresos con ello. ¿Te lo contamos?",
        "cierre_boton": "🤝 Sí, cuéntame cómo",
        "pie_texto": "¿Buscas una oportunidad profesional en lugar de ahorrar?",
        "pie_boton": "🤝 Únete al equipo",
        "equipo_titulo": "🤝 Únete al equipo",
        "equipo_intro": "¿Te gustaría **generar ingresos** ayudando a otras personas "
                        "a ahorrar? Déjanos tus datos y te contamos cómo funciona, "
                        "sin compromiso.",
        "equipo_ciudad": "Ciudad",
        "equipo_situacion": "¿Cuál es tu situación actual?",
        "situacion_opts": ["Busco empleo", "Quiero ingresos extra",
                           "Ya trabajo como autónomo/a", "Otra"],
        "equipo_experiencia": "¿Tienes experiencia en ventas o atención al cliente?",
        "experiencia_opts": ["Ninguna", "Ventas / comercial", "Seguros",
                             "Energía o telecomunicaciones", "Otra"],
        "equipo_disponibilidad": "¿Qué disponibilidad tienes?",
        "disponibilidad_opts": ["Tiempo completo", "Media jornada",
                                "Solo algunas horas"],
        "equipo_mensaje": "¿Algo que quieras contarnos? (opcional)",
        "equipo_consent": "Acepto que mis datos se usen para contactarme "
                          "sobre esta oportunidad *",
        "equipo_boton": "🚀 Quiero más información",
        "equipo_gracias": "¡Gracias, {nombre}! 🙌 Te contactaremos pronto "
                          "para contarte más.",
    },
    "en": {
        "idioma_label": "🌍 Language",
        "titulo": "💡 Are you paying too much?",
        "subtitulo": "Compare and save on your household services",
        "intro": "Leave us your details and an advisor will prepare a "
                 "**free, no-obligation** proposal for you.",
        "prog1": "Step 1 of 3 · Choose your services",
        "prog2": "Step 2 of 3 · Tell us what you pay",
        "prog3": "Completed! 🎉",
        "paso1_titulo": "1️⃣ What would you like to save on?",
        "elige": "Choose one or more services",
        "aviso_elige": "👆 Choose at least one service to continue.",
        "paso2_titulo": "2️⃣ How much do you pay per month?",
        "aprox": "An approximate figure is enough. If you don't know, leave it at 0.",
        "pagas_mes": "You pay per month",
        "pagas_anio": "You pay per year",
        "veamos": "Let's see how much of this we can reduce. 👇",
        "paso3_titulo": "3️⃣ Where shall we send your proposal?",
        "nombre": "Name *",
        "prefijo": "Country code",
        "telefono": "Phone / WhatsApp *",
        "email": "Email (optional)",
        "ciudad": "City or postcode",
        "horario": "When would you prefer to be contacted?",
        "horario_opts": ["No preference", "Morning", "Afternoon"],
        "consent": "I agree to my data being used to contact me "
                   "with a personalised proposal *",
        "boton_enviar": "💰 I want my free proposal",
        "err_nombre": "Please enter your name.",
        "err_telefono": "Please enter a valid phone number (6 to 14 digits).",
        "err_email": "That email doesn't look valid.",
        "err_consent": "You must accept the use of your data so we can contact you.",
        "gracias": "Thank you, {nombre}! 🎉 An advisor will contact you soon "
                   "with your proposal.",
        "cierre_titulo": "💼 One last thing...",
        "cierre_texto": "Many people who start by saving end up **helping others "
                        "save** and earning an income from it. Shall we tell you more?",
        "cierre_boton": "🤝 Yes, tell me more",
        "pie_texto": "Looking for a professional opportunity instead of savings?",
        "pie_boton": "🤝 Join the team",
        "equipo_titulo": "🤝 Join the team",
        "equipo_intro": "Would you like to **earn an income** helping other people "
                        "save? Leave us your details and we'll explain how it works, "
                        "with no obligation.",
        "equipo_ciudad": "City",
        "equipo_situacion": "What is your current situation?",
        "situacion_opts": ["Looking for a job", "I want extra income",
                           "I already work as a freelancer", "Other"],
        "equipo_experiencia": "Do you have experience in sales or customer service?",
        "experiencia_opts": ["None", "Sales", "Insurance",
                             "Energy or telecoms", "Other"],
        "equipo_disponibilidad": "What availability do you have?",
        "disponibilidad_opts": ["Full time", "Part time", "Just a few hours"],
        "equipo_mensaje": "Anything you'd like to tell us? (optional)",
        "equipo_consent": "I agree to my data being used to contact me "
                          "about this opportunity *",
        "equipo_boton": "🚀 I want more information",
        "equipo_gracias": "Thank you, {nombre}! 🙌 We'll contact you soon "
                          "to tell you more.",
    },
}


def t(idioma, clave):
    """Devuelve un texto en el idioma elegido.
    Si falta la traducción, usa el castellano para que nunca salga vacío."""
    return TEXTOS.get(idioma, TEXTOS["es"]).get(clave, TEXTOS["es"][clave])


def servicios(idioma):
    """Devuelve la lista de servicios traducidos, en orden."""
    traducciones = SERVICIOS.get(idioma, SERVICIOS["es"])
    return [traducciones[clave] for clave in CLAVES_SERVICIOS]