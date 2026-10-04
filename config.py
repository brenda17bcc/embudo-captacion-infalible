"""Datos del asesor y ajustes visuales del embudo.

👉 ESTE ES EL ÚNICO ARCHIVO QUE HAY QUE TOCAR PARA PERSONALIZAR LA APP.
No hace falta saber programar: solo cambia el texto entre comillas.
"""

# ---------------------------------------------------------------
# 1. PALETA DE COLORES
#    Opciones: "marca" | "verde" | "oscuro" | "azul"
#    Cambia esta palabra y REINICIA la app (Ctrl+C y streamlit run app.py).
# ---------------------------------------------------------------
PALETA = "marca"

# ---------------------------------------------------------------
# 2. DATOS DEL ASESOR
# ---------------------------------------------------------------
NOMBRE = "Javier Criao"

# Marca personal (nunca logos ni nombres de las empresas con las que colabora)
MARCA = "Casa Criao"

# Logo completo (casa + "Casa Criao" + claim). Debe estar en esta carpeta.
LOGO = "logo.png"

# Versión clara del logo, para la paleta de fondo oscuro.
LOGO_CLARO = "logo_claro.png"

# Solo el icono de la casa: se usa de marca de agua de fondo y en el pie.
ICONO = "logo_icono.png"

# Foto: pon el archivo en la misma carpeta del proyecto.
# Si el archivo no existe, la app muestra un icono y no se rompe.
FOTO = "foto.png"

# WhatsApp: solo números, con prefijo del país y SIN "+" ni espacios.
# Ejemplo España: 34600112233
WHATSAPP = "34600620864"

EMAIL = "javierasr@casacriao.com"

ZONA = "Barcelona y toda España"

# ---------------------------------------------------------------
# 3. FRASE DE PRESENTACIÓN (una por idioma)
#    Si falta un idioma, se usa el castellano automáticamente.
# ---------------------------------------------------------------
CLAIM = {
    "es": "Asesor independiente. Te ayudo a pagar menos en tus servicios.",
    "ca": "Assessor independent. T'ajudo a pagar menys en els teus serveis.",
    "en": "Independent advisor. I help you pay less for your services.",
    "pt": "Consultor independente. Ajudo-o a pagar menos pelos seus serviços.",
    "fr": "Conseiller indépendant. Je vous aide à payer moins vos services.",
    "it": "Consulente indipendente. Ti aiuto a pagare meno i tuoi servizi.",
    "de": "Unabhängiger Berater. Ich helfe Ihnen, weniger zu zahlen.",
}

# Frase para el embudo de vivienda (compra, venta y alquiler)
CLAIM_INMO = {
    "es": "Asesor inmobiliario. Te acompaño en la compra o venta de tu vivienda.",
    "ca": "Assessor immobiliari. T'acompanyo en la compra o venda del teu habitatge.",
    "en": "Property advisor. I guide you through buying or selling your home.",
    "pt": "Consultor imobiliário. Acompanho-o na compra ou venda da sua casa.",
    "fr": "Conseiller immobilier. Je vous accompagne pour acheter ou vendre "
          "votre logement.",
    "it": "Consulente immobiliare. Ti accompagno nell'acquisto o nella vendita "
          "della tua casa.",
    "de": "Immobilienberater. Ich begleite Sie beim Kauf oder Verkauf Ihrer "
          "Immobilie.",
}

# ---------------------------------------------------------------
# 4. DATOS PARA LA POLÍTICA DE PRIVACIDAD (obligatorio por el RGPD)
#    Responsable = quien guarda los datos: nombre y NIF o nombre fiscal.
# ---------------------------------------------------------------
# En la página solo se muestran el nombre y la marca: el NIF NO se publica.
# Si alguien lo solicita por email, se le facilita de forma privada.
RESPONSABLE_DATOS = "Javier Criao — Casa Criao"
EMAIL_PRIVACIDAD = "javierasr@casacriao.com"
