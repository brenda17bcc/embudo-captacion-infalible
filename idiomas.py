"""Textos de la app en varios idiomas (internacionalización).

Embudo de Captación Infalible
Idiomas: castellano, catalán, inglés, portugués, francés, italiano y alemán.
"""

# Idiomas disponibles: lo que ve el usuario -> código interno
IDIOMAS = {
    "🇪🇸 Castellano": "es",
    "🏴 Català": "ca",
    "🇬🇧 English": "en",
    "🇵🇹 Português": "pt",
    "🇫🇷 Français": "fr",
    "🇮🇹 Italiano": "it",
    "🇩🇪 Deutsch": "de",
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
    "ca": {
        "medico": "🏥 Assegurança mèdica",
        "dental": "🦷 Assegurança dental",
        "coche": "🚗 Assegurança de cotxe",
        "luz": "💡 Llum",
        "internet": "🌐 Internet",
        "tv": "📺 TV / Cable",
        "movil": "📱 Mòbil",
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
    "pt": {
        "medico": "🏥 Seguro de saúde",
        "dental": "🦷 Seguro dentário",
        "coche": "🚗 Seguro automóvel",
        "luz": "💡 Eletricidade",
        "internet": "🌐 Internet",
        "tv": "📺 TV / Cabo",
        "movil": "📱 Telemóvel",
        "hipoteca": "🏠 Crédito habitação",
    },
    "fr": {
        "medico": "🏥 Assurance santé",
        "dental": "🦷 Assurance dentaire",
        "coche": "🚗 Assurance auto",
        "luz": "💡 Électricité",
        "internet": "🌐 Internet",
        "tv": "📺 TV / Câble",
        "movil": "📱 Mobile",
        "hipoteca": "🏠 Prêt immobilier",
    },
    "it": {
        "medico": "🏥 Assicurazione sanitaria",
        "dental": "🦷 Assicurazione dentistica",
        "coche": "🚗 Assicurazione auto",
        "luz": "💡 Luce",
        "internet": "🌐 Internet",
        "tv": "📺 TV / Cavo",
        "movil": "📱 Cellulare",
        "hipoteca": "🏠 Mutuo",
    },
    "de": {
        "medico": "🏥 Krankenversicherung",
        "dental": "🦷 Zahnversicherung",
        "coche": "🚗 Kfz-Versicherung",
        "luz": "💡 Strom",
        "internet": "🌐 Internet",
        "tv": "📺 TV / Kabel",
        "movil": "📱 Handy",
        "hipoteca": "🏠 Hypothek",
    },
}

# Todos los textos de la app
TEXTOS = {
    # ------------------------------------------------ CASTELLANO
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
        "placeholder": "Elige una o varias opciones",
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
        "err_consent": "Debes aceptar el uso de tus datos para que podamos "
                       "contactarte.",
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
        "como_funciona": "Cómo funciona",
        "paso_a_t": "1. Cuéntanos qué pagas",
        "paso_a_d": "Rellenas el formulario en un minuto, sin compromiso.",
        "paso_b_t": "2. Comparamos por ti",
        "paso_b_d": "Revisamos tus servicios y buscamos mejores condiciones.",
        "paso_c_t": "3. Tú decides",
        "paso_c_d": "Te llamamos con la propuesta. Si no te convence, "
                    "no cambias nada.",
        "sello_seguridad": "🔒 Nunca pedimos datos bancarios, DNI ni contraseñas",
        "sello_gratis": "✅ Gratis y sin compromiso",
        "sello_persona": "👤 Te atiende una persona, no un robot",
        "contacto_directo": "¿Prefieres hablar directamente?",
        "whatsapp_boton": "💬 Escríbeme por WhatsApp",
        "wa_mensaje": "Hola, me gustaría información para ahorrar en mis servicios.",
        "privacidad_titulo": "🔐 Cómo tratamos tus datos",
        "privacidad_texto": (
            "**Responsable del tratamiento:** {responsable}\n\n"
            "**Finalidad:** contactarte para preparar una propuesta de ahorro "
            "personalizada o informarte sobre la oportunidad profesional.\n\n"
            "**Base legal:** tu consentimiento, que puedes retirar cuando "
            "quieras.\n\n"
            "**Conservación:** guardamos tus datos mientras dure la relación o "
            "hasta que solicites su supresión.\n\n"
            "**Cesiones:** no vendemos tus datos ni los cedemos a terceros "
            "ajenos a la gestión de tu propuesta.\n\n"
            "**Tus derechos:** puedes acceder, rectificar, suprimir u oponerte "
            "al tratamiento escribiendo a {email}."
        ),
    },
    # ------------------------------------------------ CATALÁN
    "ca": {
        "idioma_label": "🌍 Idioma",
        "titulo": "💡 Estàs pagant de més?",
        "subtitulo": "Compara i estalvia en els teus serveis de la llar",
        "intro": "Deixa'ns les teves dades i un assessor et prepararà una proposta "
                 "**gratuïta i sense compromís**.",
        "prog1": "Pas 1 de 3 · Tria els teus serveis",
        "prog2": "Pas 2 de 3 · Digues-nos quant pagues",
        "prog3": "Completat! 🎉",
        "paso1_titulo": "1️⃣ En què t'agradaria estalviar?",
        "elige": "Tria un o diversos serveis",
        "placeholder": "Tria una o diverses opcions",
        "aviso_elige": "👆 Tria almenys un servei per continuar.",
        "paso2_titulo": "2️⃣ Quant pagues ara al mes?",
        "aprox": "Un valor aproximat és suficient. Si no ho saps, deixa-ho a 0.",
        "pagas_mes": "Pagues al mes",
        "pagas_anio": "Pagues a l'any",
        "veamos": "Vegem quant d'això podem reduir. 👇",
        "paso3_titulo": "3️⃣ On t'enviem la proposta?",
        "nombre": "Nom *",
        "prefijo": "Prefix",
        "telefono": "Telèfon / WhatsApp *",
        "email": "Correu electrònic (opcional)",
        "ciudad": "Ciutat o codi postal",
        "horario": "Quan prefereixes que et contactem?",
        "horario_opts": ["Indiferent", "Matí", "Tarda"],
        "consent": "Accepto que les meves dades s'utilitzin per contactar-me "
                   "amb una proposta personalitzada *",
        "boton_enviar": "💰 Vull la meva proposta gratuïta",
        "err_nombre": "Escriu el teu nom.",
        "err_telefono": "Escriu un telèfon vàlid (entre 6 i 14 dígits).",
        "err_email": "El correu electrònic no sembla vàlid.",
        "err_consent": "Has d'acceptar l'ús de les teves dades perquè puguem "
                       "contactar-te.",
        "gracias": "Gràcies, {nombre}! 🎉 Un assessor et contactarà aviat "
                   "amb la teva proposta.",
        "cierre_titulo": "💼 Una última cosa...",
        "cierre_texto": "Molta gent que comença estalviant acaba **ajudant altres "
                        "a estalviar** i generant ingressos amb això. T'ho expliquem?",
        "cierre_boton": "🤝 Sí, explica-m'ho",
        "pie_texto": "Busques una oportunitat professional en lloc d'estalviar?",
        "pie_boton": "🤝 Uneix-te a l'equip",
        "equipo_titulo": "🤝 Uneix-te a l'equip",
        "equipo_intro": "T'agradaria **generar ingressos** ajudant altres persones "
                        "a estalviar? Deixa'ns les teves dades i t'expliquem com "
                        "funciona, sense compromís.",
        "equipo_ciudad": "Ciutat",
        "equipo_situacion": "Quina és la teva situació actual?",
        "situacion_opts": ["Busco feina", "Vull ingressos extra",
                           "Ja treballo com a autònom/a", "Una altra"],
        "equipo_experiencia": "Tens experiència en vendes o atenció al client?",
        "experiencia_opts": ["Cap", "Vendes / comercial", "Assegurances",
                             "Energia o telecomunicacions", "Una altra"],
        "equipo_disponibilidad": "Quina disponibilitat tens?",
        "disponibilidad_opts": ["Jornada completa", "Mitja jornada",
                                "Només algunes hores"],
        "equipo_mensaje": "Alguna cosa que ens vulguis explicar? (opcional)",
        "equipo_consent": "Accepto que les meves dades s'utilitzin per contactar-me "
                          "sobre aquesta oportunitat *",
        "equipo_boton": "🚀 Vull més informació",
        "equipo_gracias": "Gràcies, {nombre}! 🙌 Et contactarem aviat "
                          "per explicar-te'n més.",
        "como_funciona": "Com funciona",
        "paso_a_t": "1. Digues-nos què pagues",
        "paso_a_d": "Omples el formulari en un minut, sense compromís.",
        "paso_b_t": "2. Comparem per tu",
        "paso_b_d": "Revisem els teus serveis i busquem millors condicions.",
        "paso_c_t": "3. Tu decideixes",
        "paso_c_d": "Et truquem amb la proposta. Si no et convenç, "
                    "no canvies res.",
        "sello_seguridad": "🔒 Mai demanem dades bancàries, DNI ni contrasenyes",
        "sello_gratis": "✅ Gratuït i sense compromís",
        "sello_persona": "👤 T'atén una persona, no un robot",
        "contacto_directo": "Prefereixes parlar directament?",
        "whatsapp_boton": "💬 Escriu-me per WhatsApp",
        "wa_mensaje": "Hola, m'agradaria informació per estalviar en els meus "
                      "serveis.",
        "privacidad_titulo": "🔐 Com tractem les teves dades",
        "privacidad_texto": (
            "**Responsable del tractament:** {responsable}\n\n"
            "**Finalitat:** contactar-te per preparar una proposta d'estalvi "
            "personalitzada o informar-te sobre l'oportunitat professional.\n\n"
            "**Base legal:** el teu consentiment, que pots retirar quan "
            "vulguis.\n\n"
            "**Conservació:** guardem les teves dades mentre duri la relació o "
            "fins que en sol·licitis la supressió.\n\n"
            "**Cessions:** no venem les teves dades ni les cedim a tercers "
            "aliens a la gestió de la teva proposta.\n\n"
            "**Els teus drets:** pots accedir, rectificar, suprimir o oposar-te "
            "al tractament escrivint a {email}."
        ),
    },
    # ------------------------------------------------ INGLÉS
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
        "placeholder": "Choose one or more options",
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
        "como_funciona": "How it works",
        "paso_a_t": "1. Tell us what you pay",
        "paso_a_d": "Fill in the form in one minute, with no obligation.",
        "paso_b_t": "2. We compare for you",
        "paso_b_d": "We review your services and look for better conditions.",
        "paso_c_t": "3. You decide",
        "paso_c_d": "We call you with the proposal. If you don't like it, "
                    "nothing changes.",
        "sello_seguridad": "🔒 We never ask for bank details, ID or passwords",
        "sello_gratis": "✅ Free and with no obligation",
        "sello_persona": "👤 A real person, not a bot",
        "contacto_directo": "Prefer to talk directly?",
        "whatsapp_boton": "💬 Message me on WhatsApp",
        "wa_mensaje": "Hello, I would like information about saving on my services.",
        "privacidad_titulo": "🔐 How we handle your data",
        "privacidad_texto": (
            "**Data controller:** {responsable}\n\n"
            "**Purpose:** to contact you to prepare a personalised savings "
            "proposal or to tell you about the professional opportunity.\n\n"
            "**Legal basis:** your consent, which you may withdraw at any "
            "time.\n\n"
            "**Retention:** we keep your data for as long as the relationship "
            "lasts or until you ask us to delete it.\n\n"
            "**Sharing:** we do not sell your data or share it with third "
            "parties outside the handling of your proposal.\n\n"
            "**Your rights:** you may access, correct, delete or object to the "
            "processing of your data by writing to {email}."
        ),
    },
    # ------------------------------------------------ PORTUGUÉS
    "pt": {
        "idioma_label": "🌍 Idioma",
        "titulo": "💡 Está a pagar demais?",
        "subtitulo": "Compare e poupe nos seus serviços domésticos",
        "intro": "Deixe-nos os seus dados e um consultor preparará uma proposta "
                 "**gratuita e sem compromisso**.",
        "prog1": "Passo 1 de 3 · Escolha os seus serviços",
        "prog2": "Passo 2 de 3 · Diga-nos quanto paga",
        "prog3": "Concluído! 🎉",
        "paso1_titulo": "1️⃣ Em que gostaria de poupar?",
        "elige": "Escolha um ou vários serviços",
        "placeholder": "Escolha uma ou várias opções",
        "aviso_elige": "👆 Escolha pelo menos um serviço para continuar.",
        "paso2_titulo": "2️⃣ Quanto paga por mês?",
        "aprox": "Um valor aproximado é suficiente. Se não souber, deixe em 0.",
        "pagas_mes": "Paga por mês",
        "pagas_anio": "Paga por ano",
        "veamos": "Vamos ver quanto disto podemos reduzir. 👇",
        "paso3_titulo": "3️⃣ Para onde enviamos a sua proposta?",
        "nombre": "Nome *",
        "prefijo": "Indicativo",
        "telefono": "Telefone / WhatsApp *",
        "email": "Email (opcional)",
        "ciudad": "Cidade ou código postal",
        "horario": "Quando prefere que o contactemos?",
        "horario_opts": ["Indiferente", "Manhã", "Tarde"],
        "consent": "Aceito que os meus dados sejam usados para me contactarem "
                   "com uma proposta personalizada *",
        "boton_enviar": "💰 Quero a minha proposta gratuita",
        "err_nombre": "Escreva o seu nome.",
        "err_telefono": "Escreva um telefone válido (entre 6 e 14 dígitos).",
        "err_email": "O email não parece válido.",
        "err_consent": "Tem de aceitar a utilização dos seus dados para podermos "
                       "contactá-lo.",
        "gracias": "Obrigado, {nombre}! 🎉 Um consultor entrará em contacto "
                   "em breve com a sua proposta.",
        "cierre_titulo": "💼 Uma última coisa...",
        "cierre_texto": "Muitas pessoas que começam por poupar acabam a **ajudar "
                        "outros a poupar** e a gerar rendimento com isso. "
                        "Quer saber mais?",
        "cierre_boton": "🤝 Sim, conte-me mais",
        "pie_texto": "Procura uma oportunidade profissional em vez de poupança?",
        "pie_boton": "🤝 Junte-se à equipa",
        "equipo_titulo": "🤝 Junte-se à equipa",
        "equipo_intro": "Gostaria de **gerar rendimento** ajudando outras pessoas "
                        "a poupar? Deixe-nos os seus dados e explicamos como "
                        "funciona, sem compromisso.",
        "equipo_ciudad": "Cidade",
        "equipo_situacion": "Qual é a sua situação atual?",
        "situacion_opts": ["Procuro emprego", "Quero rendimento extra",
                           "Já trabalho como independente", "Outra"],
        "equipo_experiencia": "Tem experiência em vendas ou atendimento ao cliente?",
        "experiencia_opts": ["Nenhuma", "Vendas / comercial", "Seguros",
                             "Energia ou telecomunicações", "Outra"],
        "equipo_disponibilidad": "Que disponibilidade tem?",
        "disponibilidad_opts": ["Tempo inteiro", "Meio período",
                                "Apenas algumas horas"],
        "equipo_mensaje": "Algo que nos queira contar? (opcional)",
        "equipo_consent": "Aceito que os meus dados sejam usados para me contactarem "
                          "sobre esta oportunidade *",
        "equipo_boton": "🚀 Quero mais informações",
        "equipo_gracias": "Obrigado, {nombre}! 🙌 Entraremos em contacto em breve "
                          "para lhe contar mais.",
        "como_funciona": "Como funciona",
        "paso_a_t": "1. Diga-nos quanto paga",
        "paso_a_d": "Preenche o formulário num minuto, sem compromisso.",
        "paso_b_t": "2. Comparamos por si",
        "paso_b_d": "Analisamos os seus serviços e procuramos melhores condições.",
        "paso_c_t": "3. Você decide",
        "paso_c_d": "Ligamos-lhe com a proposta. Se não gostar, "
                    "não muda nada.",
        "sello_seguridad": "🔒 Nunca pedimos dados bancários, documentos "
                           "de identificação nem palavras-passe",
        "sello_gratis": "✅ Gratuito e sem compromisso",
        "sello_persona": "👤 Atende-o uma pessoa, não um robô",
        "contacto_directo": "Prefere falar diretamente?",
        "whatsapp_boton": "💬 Fale comigo pelo WhatsApp",
        "wa_mensaje": "Olá, gostaria de informações para poupar nos meus serviços.",
        "privacidad_titulo": "🔐 Como tratamos os seus dados",
        "privacidad_texto": (
            "**Responsável pelo tratamento:** {responsable}\n\n"
            "**Finalidade:** contactá-lo para preparar uma proposta de poupança "
            "personalizada ou informá-lo sobre a oportunidade profissional.\n\n"
            "**Base legal:** o seu consentimento, que pode retirar a qualquer "
            "momento.\n\n"
            "**Conservação:** guardamos os seus dados enquanto durar a relação "
            "ou até que solicite a sua eliminação.\n\n"
            "**Partilha:** não vendemos os seus dados nem os cedemos a "
            "terceiros alheios à gestão da sua proposta.\n\n"
            "**Os seus direitos:** pode aceder, retificar, eliminar ou opor-se "
            "ao tratamento escrevendo para {email}."
        ),
    },
    # ------------------------------------------------ FRANCÉS
    "fr": {
        "idioma_label": "🌍 Langue",
        "titulo": "💡 Vous payez trop cher ?",
        "subtitulo": "Comparez et économisez sur vos services du quotidien",
        "intro": "Laissez-nous vos coordonnées et un conseiller vous préparera "
                 "une proposition **gratuite et sans engagement**.",
        "prog1": "Étape 1 sur 3 · Choisissez vos services",
        "prog2": "Étape 2 sur 3 · Dites-nous combien vous payez",
        "prog3": "Terminé ! 🎉",
        "paso1_titulo": "1️⃣ Sur quoi aimeriez-vous économiser ?",
        "elige": "Choisissez un ou plusieurs services",
        "placeholder": "Choisissez une ou plusieurs options",
        "aviso_elige": "👆 Choisissez au moins un service pour continuer.",
        "paso2_titulo": "2️⃣ Combien payez-vous par mois ?",
        "aprox": "Un montant approximatif suffit. Si vous ne savez pas, laissez 0.",
        "pagas_mes": "Vous payez par mois",
        "pagas_anio": "Vous payez par an",
        "veamos": "Voyons combien nous pouvons réduire. 👇",
        "paso3_titulo": "3️⃣ Où envoyons-nous votre proposition ?",
        "nombre": "Nom *",
        "prefijo": "Indicatif",
        "telefono": "Téléphone / WhatsApp *",
        "email": "E-mail (facultatif)",
        "ciudad": "Ville ou code postal",
        "horario": "Quand préférez-vous être contacté ?",
        "horario_opts": ["Peu importe", "Le matin", "L'après-midi"],
        "consent": "J'accepte que mes données soient utilisées pour me contacter "
                   "avec une proposition personnalisée *",
        "boton_enviar": "💰 Je veux ma proposition gratuite",
        "err_nombre": "Veuillez saisir votre nom.",
        "err_telefono": "Veuillez saisir un téléphone valide (6 à 14 chiffres).",
        "err_email": "L'e-mail ne semble pas valide.",
        "err_consent": "Vous devez accepter l'utilisation de vos données pour que "
                       "nous puissions vous contacter.",
        "gracias": "Merci, {nombre} ! 🎉 Un conseiller vous contactera bientôt "
                   "avec votre proposition.",
        "cierre_titulo": "💼 Une dernière chose...",
        "cierre_texto": "Beaucoup de personnes qui commencent par économiser "
                        "finissent par **aider les autres à économiser** et à en "
                        "tirer un revenu. On vous explique ?",
        "cierre_boton": "🤝 Oui, dites-m'en plus",
        "pie_texto": "Vous cherchez une opportunité professionnelle ?",
        "pie_boton": "🤝 Rejoignez l'équipe",
        "equipo_titulo": "🤝 Rejoignez l'équipe",
        "equipo_intro": "Aimeriez-vous **générer des revenus** en aidant d'autres "
                        "personnes à économiser ? Laissez-nous vos coordonnées et "
                        "nous vous expliquons comment cela fonctionne, "
                        "sans engagement.",
        "equipo_ciudad": "Ville",
        "equipo_situacion": "Quelle est votre situation actuelle ?",
        "situacion_opts": ["Je cherche un emploi", "Je veux un revenu complémentaire",
                           "Je suis déjà indépendant(e)", "Autre"],
        "equipo_experiencia": "Avez-vous de l'expérience en vente ou relation client ?",
        "experiencia_opts": ["Aucune", "Vente / commercial", "Assurances",
                             "Énergie ou télécoms", "Autre"],
        "equipo_disponibilidad": "Quelle est votre disponibilité ?",
        "disponibilidad_opts": ["Temps plein", "Temps partiel",
                                "Quelques heures seulement"],
        "equipo_mensaje": "Quelque chose à nous dire ? (facultatif)",
        "equipo_consent": "J'accepte que mes données soient utilisées pour me "
                          "contacter au sujet de cette opportunité *",
        "equipo_boton": "🚀 Je veux plus d'informations",
        "equipo_gracias": "Merci, {nombre} ! 🙌 Nous vous contacterons bientôt "
                          "pour vous en dire plus.",
        "como_funciona": "Comment ça marche",
        "paso_a_t": "1. Dites-nous ce que vous payez",
        "paso_a_d": "Vous remplissez le formulaire en une minute, sans engagement.",
        "paso_b_t": "2. Nous comparons pour vous",
        "paso_b_d": "Nous étudions vos services et cherchons de meilleures "
                    "conditions.",
        "paso_c_t": "3. Vous décidez",
        "paso_c_d": "Nous vous appelons avec la proposition. Si elle ne vous "
                    "convient pas, rien ne change.",
        "sello_seguridad": "🔒 Nous ne demandons jamais vos coordonnées "
                           "bancaires, pièce d'identité ou mots de passe",
        "sello_gratis": "✅ Gratuit et sans engagement",
        "sello_persona": "👤 Une vraie personne, pas un robot",
        "contacto_directo": "Vous préférez parler directement ?",
        "whatsapp_boton": "💬 Écrivez-moi sur WhatsApp",
        "wa_mensaje": "Bonjour, je souhaiterais des informations pour économiser "
                      "sur mes services.",
        "privacidad_titulo": "🔐 Comment nous traitons vos données",
        "privacidad_texto": (
            "**Responsable du traitement :** {responsable}\n\n"
            "**Finalité :** vous contacter pour préparer une proposition "
            "d'économies personnalisée ou vous informer sur l'opportunité "
            "professionnelle.\n\n"
            "**Base légale :** votre consentement, que vous pouvez retirer à "
            "tout moment.\n\n"
            "**Conservation :** nous conservons vos données pendant la durée de "
            "la relation ou jusqu'à votre demande de suppression.\n\n"
            "**Transmission :** nous ne vendons pas vos données et ne les "
            "cédons pas à des tiers étrangers à la gestion de votre "
            "proposition.\n\n"
            "**Vos droits :** vous pouvez accéder à vos données, les rectifier, "
            "les supprimer ou vous opposer à leur traitement en écrivant à "
            "{email}."
        ),
    },
    # ------------------------------------------------ ITALIANO
    "it": {
        "idioma_label": "🌍 Lingua",
        "titulo": "💡 Stai pagando troppo?",
        "subtitulo": "Confronta e risparmia sui servizi di casa",
        "intro": "Lasciaci i tuoi dati e un consulente ti preparerà una proposta "
                 "**gratuita e senza impegno**.",
        "prog1": "Passo 1 di 3 · Scegli i tuoi servizi",
        "prog2": "Passo 2 di 3 · Dicci quanto paghi",
        "prog3": "Completato! 🎉",
        "paso1_titulo": "1️⃣ Su cosa vorresti risparmiare?",
        "elige": "Scegli uno o più servizi",
        "placeholder": "Scegli una o più opzioni",
        "aviso_elige": "👆 Scegli almeno un servizio per continuare.",
        "paso2_titulo": "2️⃣ Quanto paghi al mese?",
        "aprox": "Un valore approssimativo è sufficiente. Se non lo sai, lascia 0.",
        "pagas_mes": "Paghi al mese",
        "pagas_anio": "Paghi all'anno",
        "veamos": "Vediamo quanto possiamo ridurre. 👇",
        "paso3_titulo": "3️⃣ Dove ti inviamo la proposta?",
        "nombre": "Nome *",
        "prefijo": "Prefisso",
        "telefono": "Telefono / WhatsApp *",
        "email": "Email (facoltativa)",
        "ciudad": "Città o CAP",
        "horario": "Quando preferisci essere contattato?",
        "horario_opts": ["Indifferente", "Mattina", "Pomeriggio"],
        "consent": "Accetto che i miei dati siano usati per contattarmi con una "
                   "proposta personalizzata *",
        "boton_enviar": "💰 Voglio la mia proposta gratuita",
        "err_nombre": "Scrivi il tuo nome.",
        "err_telefono": "Scrivi un telefono valido (tra 6 e 14 cifre).",
        "err_email": "L'email non sembra valida.",
        "err_consent": "Devi accettare l'uso dei tuoi dati per poterti contattare.",
        "gracias": "Grazie, {nombre}! 🎉 Un consulente ti contatterà presto "
                   "con la tua proposta.",
        "cierre_titulo": "💼 Un'ultima cosa...",
        "cierre_texto": "Molte persone che iniziano risparmiando finiscono per "
                        "**aiutare altri a risparmiare** e a generare un reddito. "
                        "Te lo raccontiamo?",
        "cierre_boton": "🤝 Sì, raccontami di più",
        "pie_texto": "Cerchi un'opportunità professionale?",
        "pie_boton": "🤝 Unisciti al team",
        "equipo_titulo": "🤝 Unisciti al team",
        "equipo_intro": "Ti piacerebbe **generare un reddito** aiutando altre "
                        "persone a risparmiare? Lasciaci i tuoi dati e ti spieghiamo "
                        "come funziona, senza impegno.",
        "equipo_ciudad": "Città",
        "equipo_situacion": "Qual è la tua situazione attuale?",
        "situacion_opts": ["Cerco lavoro", "Voglio un reddito extra",
                           "Lavoro già come libero professionista", "Altro"],
        "equipo_experiencia": "Hai esperienza nelle vendite o nel servizio clienti?",
        "experiencia_opts": ["Nessuna", "Vendite / commerciale", "Assicurazioni",
                             "Energia o telecomunicazioni", "Altro"],
        "equipo_disponibilidad": "Che disponibilità hai?",
        "disponibilidad_opts": ["Tempo pieno", "Part time", "Solo alcune ore"],
        "equipo_mensaje": "Qualcosa che vuoi dirci? (facoltativo)",
        "equipo_consent": "Accetto che i miei dati siano usati per contattarmi "
                          "riguardo a questa opportunità *",
        "equipo_boton": "🚀 Voglio più informazioni",
        "equipo_gracias": "Grazie, {nombre}! 🙌 Ti contatteremo presto "
                          "per dirti di più.",
        "como_funciona": "Come funziona",
        "paso_a_t": "1. Dicci quanto paghi",
        "paso_a_d": "Compili il modulo in un minuto, senza impegno.",
        "paso_b_t": "2. Confrontiamo per te",
        "paso_b_d": "Esaminiamo i tuoi servizi e cerchiamo condizioni migliori.",
        "paso_c_t": "3. Decidi tu",
        "paso_c_d": "Ti chiamiamo con la proposta. Se non ti convince, "
                    "non cambia nulla.",
        "sello_seguridad": "🔒 Non chiediamo mai dati bancari, documenti "
                           "d'identità o password",
        "sello_gratis": "✅ Gratuito e senza impegno",
        "sello_persona": "👤 Ti risponde una persona, non un robot",
        "contacto_directo": "Preferisci parlare direttamente?",
        "whatsapp_boton": "💬 Scrivimi su WhatsApp",
        "wa_mensaje": "Ciao, vorrei informazioni per risparmiare sui miei servizi.",
        "privacidad_titulo": "🔐 Come trattiamo i tuoi dati",
        "privacidad_texto": (
            "**Titolare del trattamento:** {responsable}\n\n"
            "**Finalità:** contattarti per preparare una proposta di risparmio "
            "personalizzata o informarti sull'opportunità professionale.\n\n"
            "**Base giuridica:** il tuo consenso, che puoi revocare in "
            "qualsiasi momento.\n\n"
            "**Conservazione:** conserviamo i tuoi dati per la durata del "
            "rapporto o fino a quando ne chiedi la cancellazione.\n\n"
            "**Comunicazione a terzi:** non vendiamo i tuoi dati né li cediamo "
            "a terzi estranei alla gestione della tua proposta.\n\n"
            "**I tuoi diritti:** puoi accedere, rettificare, cancellare o "
            "opporti al trattamento scrivendo a {email}."
        ),
    },
    # ------------------------------------------------ ALEMÁN
    "de": {
        "idioma_label": "🌍 Sprache",
        "titulo": "💡 Zahlen Sie zu viel?",
        "subtitulo": "Vergleichen und sparen Sie bei Ihren Haushaltsdiensten",
        "intro": "Hinterlassen Sie uns Ihre Daten und ein Berater erstellt Ihnen "
                 "ein **kostenloses und unverbindliches** Angebot.",
        "prog1": "Schritt 1 von 3 · Wählen Sie Ihre Dienste",
        "prog2": "Schritt 2 von 3 · Sagen Sie uns, was Sie zahlen",
        "prog3": "Fertig! 🎉",
        "paso1_titulo": "1️⃣ Wobei möchten Sie sparen?",
        "elige": "Wählen Sie einen oder mehrere Dienste",
        "placeholder": "Wählen Sie eine oder mehrere Optionen",
        "aviso_elige": "👆 Wählen Sie mindestens einen Dienst, um fortzufahren.",
        "paso2_titulo": "2️⃣ Wie viel zahlen Sie monatlich?",
        "aprox": "Ein ungefährer Wert genügt. Wenn Sie es nicht wissen, "
                 "lassen Sie 0 stehen.",
        "pagas_mes": "Sie zahlen monatlich",
        "pagas_anio": "Sie zahlen jährlich",
        "veamos": "Schauen wir, wie viel davon wir senken können. 👇",
        "paso3_titulo": "3️⃣ Wohin schicken wir Ihr Angebot?",
        "nombre": "Name *",
        "prefijo": "Vorwahl",
        "telefono": "Telefon / WhatsApp *",
        "email": "E-Mail (optional)",
        "ciudad": "Stadt oder Postleitzahl",
        "horario": "Wann möchten Sie kontaktiert werden?",
        "horario_opts": ["Egal", "Vormittags", "Nachmittags"],
        "consent": "Ich stimme zu, dass meine Daten verwendet werden, um mich mit "
                   "einem persönlichen Angebot zu kontaktieren *",
        "boton_enviar": "💰 Ich möchte mein kostenloses Angebot",
        "err_nombre": "Bitte geben Sie Ihren Namen ein.",
        "err_telefono": "Bitte geben Sie eine gültige Telefonnummer ein "
                        "(6 bis 14 Ziffern).",
        "err_email": "Die E-Mail-Adresse scheint ungültig zu sein.",
        "err_consent": "Sie müssen der Nutzung Ihrer Daten zustimmen, damit wir "
                       "Sie kontaktieren können.",
        "gracias": "Danke, {nombre}! 🎉 Ein Berater meldet sich bald "
                   "mit Ihrem Angebot.",
        "cierre_titulo": "💼 Noch eine Sache...",
        "cierre_texto": "Viele, die mit dem Sparen anfangen, **helfen später "
                        "anderen beim Sparen** und verdienen damit Geld. "
                        "Sollen wir es Ihnen erklären?",
        "cierre_boton": "🤝 Ja, erzählen Sie mir mehr",
        "pie_texto": "Suchen Sie eine berufliche Chance?",
        "pie_boton": "🤝 Werden Sie Teil des Teams",
        "equipo_titulo": "🤝 Werden Sie Teil des Teams",
        "equipo_intro": "Möchten Sie **Einkommen erzielen**, indem Sie anderen beim "
                        "Sparen helfen? Hinterlassen Sie uns Ihre Daten und wir "
                        "erklären Ihnen unverbindlich, wie es funktioniert.",
        "equipo_ciudad": "Stadt",
        "equipo_situacion": "Wie ist Ihre aktuelle Situation?",
        "situacion_opts": ["Ich suche Arbeit", "Ich möchte Zusatzeinkommen",
                           "Ich bin bereits selbstständig", "Andere"],
        "equipo_experiencia": "Haben Sie Erfahrung im Vertrieb oder Kundenservice?",
        "experiencia_opts": ["Keine", "Vertrieb", "Versicherungen",
                             "Energie oder Telekommunikation", "Andere"],
        "equipo_disponibilidad": "Welche Verfügbarkeit haben Sie?",
        "disponibilidad_opts": ["Vollzeit", "Teilzeit", "Nur einige Stunden"],
        "equipo_mensaje": "Möchten Sie uns etwas mitteilen? (optional)",
        "equipo_consent": "Ich stimme zu, dass meine Daten verwendet werden, um "
                          "mich zu dieser Gelegenheit zu kontaktieren *",
        "equipo_boton": "🚀 Ich möchte mehr Informationen",
        "equipo_gracias": "Danke, {nombre}! 🙌 Wir melden uns bald, "
                          "um Ihnen mehr zu erzählen.",
        "como_funciona": "So funktioniert es",
        "paso_a_t": "1. Sagen Sie uns, was Sie zahlen",
        "paso_a_d": "Sie füllen das Formular in einer Minute aus, unverbindlich.",
        "paso_b_t": "2. Wir vergleichen für Sie",
        "paso_b_d": "Wir prüfen Ihre Verträge und suchen bessere Konditionen.",
        "paso_c_t": "3. Sie entscheiden",
        "paso_c_d": "Wir rufen Sie mit dem Angebot an. Überzeugt es nicht, "
                    "ändert sich nichts.",
        "sello_seguridad": "🔒 Wir fragen nie nach Bankdaten, Ausweis "
                           "oder Passwörtern",
        "sello_gratis": "✅ Kostenlos und unverbindlich",
        "sello_persona": "👤 Ein echter Mensch, kein Bot",
        "contacto_directo": "Möchten Sie lieber direkt sprechen?",
        "whatsapp_boton": "💬 Schreiben Sie mir per WhatsApp",
        "wa_mensaje": "Hallo, ich hätte gern Informationen, um bei meinen "
                      "Verträgen zu sparen.",
        "privacidad_titulo": "🔐 So gehen wir mit Ihren Daten um",
        "privacidad_texto": (
            "**Verantwortlicher:** {responsable}\n\n"
            "**Zweck:** Sie zu kontaktieren, um ein persönliches Sparangebot zu "
            "erstellen oder Sie über die berufliche Gelegenheit zu "
            "informieren.\n\n"
            "**Rechtsgrundlage:** Ihre Einwilligung, die Sie jederzeit "
            "widerrufen können.\n\n"
            "**Speicherdauer:** Wir speichern Ihre Daten für die Dauer der "
            "Geschäftsbeziehung oder bis Sie deren Löschung verlangen.\n\n"
            "**Weitergabe:** Wir verkaufen Ihre Daten nicht und geben sie nicht "
            "an Dritte außerhalb der Bearbeitung Ihres Angebots weiter.\n\n"
            "**Ihre Rechte:** Sie können Ihre Daten einsehen, berichtigen, "
            "löschen oder der Verarbeitung widersprechen, indem Sie an {email} "
            "schreiben."
        ),
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
