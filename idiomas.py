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