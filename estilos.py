"""Paletas de color y estilos visuales del embudo.

Todas las paletas parten de los colores reales del logo de Casa Criao:
verde bosque #1F3C33, dorado #BF8A2E y crema #F6F4EC.
"""

# Colores exactos tomados del logo
VERDE_MARCA = "#1F3C33"
DORADO_MARCA = "#BF8A2E"
CREMA_MARCA = "#F6F4EC"

PALETAS = {
    # Los colores del logo, tal cual. La más fiel a la marca.
    "marca": {
        "etiqueta": "Marca Casa Criao (crema, verde y dorado)",
        "primario": VERDE_MARCA,
        "acento": DORADO_MARCA,
        "texto_boton": "#16261F",
        "detalle": DORADO_MARCA,
        "fondo": CREMA_MARCA,
        "tarjeta": "#FFFFFF",
        "texto": "#1C2A24",
        "suave": "#6B6A5C",
        "borde": "#E6E0D2",
        "logo_claro": False,
        "texto_campo": None,
    },
    # Verde más claro y fresco, dorado en los detalles. La más legible.
    "verde": {
        "etiqueta": "Verde claro con dorado en detalles",
        "primario": VERDE_MARCA,
        "acento": "#2E7D5B",
        "texto_boton": "#FFFFFF",
        "detalle": DORADO_MARCA,
        "fondo": "#F2F7F3",
        "tarjeta": "#FFFFFF",
        "texto": "#15271F",
        "suave": "#51695D",
        "borde": "#DCE9E0",
        "logo_claro": False,
        "texto_campo": None,
    },
    # Azul marino con el dorado de la marca. Aire institucional.
    "azul": {
        "etiqueta": "Azul marino con dorado de marca",
        "primario": "#123C6B",
        "acento": DORADO_MARCA,
        "texto_boton": "#16261F",
        "detalle": DORADO_MARCA,
        "fondo": "#F5F8FC",
        "tarjeta": "#FFFFFF",
        "texto": "#12243B",
        "suave": "#5A6B82",
        "borde": "#E1E7F0",
        "logo_claro": False,
        "texto_campo": None,
    },
    # Verde muy oscuro con dorado. Elegante, muy llamativa en redes.
    "oscuro": {
        "etiqueta": "Verde oscuro premium con dorado",
        "primario": "#D9A93F",
        "acento": "#D9A93F",
        "texto_boton": "#12271F",
        "detalle": "#D9A93F",
        "fondo": "#12271F",
        "tarjeta": "#1B3328",
        "texto": "#ECF2EE",
        "suave": "#A7BCB1",
        "borde": "#27483A",
        "logo_claro": True,
        "texto_campo": "#12271F",
    },
}


def obtener_paleta(nombre):
    """Devuelve la paleta elegida. Si el nombre no existe, usa la de marca."""
    return PALETAS.get(nombre, PALETAS["marca"])


def css(p, marca_agua=None):
    """Genera la hoja de estilos.

    marca_agua: el logo en base64 para usarlo de fondo muy suave (opcional).
    """
    # En la paleta oscura los campos siguen siendo blancos: el texto va oscuro
    texto_campo = p.get("texto_campo") or "#1C2A24"
    fondo_marca_agua = ""
    if marca_agua:
        fondo_marca_agua = f"""
.stApp::before {{
    content: "";
    position: fixed;
    top: 12%;
    right: -60px;
    width: 420px;
    height: 420px;
    background-image: url("data:image/png;base64,{marca_agua}");
    background-size: contain;
    background-repeat: no-repeat;
    opacity: .05;
    pointer-events: none;
    z-index: 0;
}}
"""

    return f"""
<style>
/* ---------- BASE ---------- */
.stApp {{ background: {p['fondo']}; }}
{fondo_marca_agua}
.block-container {{
    max-width: 780px;
    padding-top: 4.4rem;
    padding-bottom: 3rem;
    position: relative;
    z-index: 1;
}}
h1, h2, h3, h4 {{ color: {p['primario']} !important; font-weight: 700 !important; }}
p, label, li, .stMarkdown {{ color: {p['texto']}; }}
[data-testid="stCaptionContainer"] p {{ color: {p['suave']}; }}

/* ---------- OCULTAR DETALLES DE STREAMLIT ---------- */
[data-testid="InputInstructions"] {{ display: none; }}
#MainMenu, footer {{ visibility: hidden; }}
[data-testid="stHeader"] {{ background: transparent; }}

/* ---------- ANIMACIONES ---------- */
@keyframes aparecer {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
.tarjeta, [data-testid="stMetric"], [data-testid="stForm"],
[data-testid="stAlertContainer"] {{
    animation: aparecer .45s ease both;
}}

/* ---------- CAMPOS DEL FORMULARIO (siempre claros) ---------- */
[data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="base-input"],
[data-baseweb="select"] > div, [data-baseweb="select"] > div > div,
.stNumberInput div[data-baseweb="input"],
[data-testid="stTextInput"] > div, [data-testid="stNumberInput"] > div,
[data-testid="stDateInput"] > div, [data-testid="stTextArea"] > div,
[data-testid="stSelectbox"] > div > div,
[data-testid="stMultiSelect"] > div > div {{
    background-color: #FFFFFF !important;
    border-color: {p['borde']} !important;
    border-radius: 10px !important;
}}
input, textarea, [data-baseweb="input"] *, [data-baseweb="select"] *,
[data-testid="stDateInput"] input {{
    color: {texto_campo} !important;
    -webkit-text-fill-color: {texto_campo} !important;
}}
[data-baseweb="select"] svg, [data-testid="stDateInput"] svg {{
    fill: {p['suave']} !important;
}}
/* listas desplegables y calendario */
[data-baseweb="popover"] div, [data-baseweb="menu"], [role="listbox"],
[data-baseweb="calendar"], [data-baseweb="calendar"] div {{
    background-color: #FFFFFF !important;
    color: {texto_campo} !important;
}}
[role="option"], [data-baseweb="menu"] li {{ color: {texto_campo} !important; }}
[role="option"]:hover, [data-baseweb="menu"] li:hover {{
    background-color: {p['fondo']} !important;
}}
[data-testid="stForm"] {{
    background: {p['tarjeta']};
    border: 1px solid {p['borde']};
    border-radius: 18px;
    padding: 20px 22px;
}}
/* etiquetas de los servicios elegidos */
[data-baseweb="tag"] {{
    background-color: {p['primario']} !important;
    border-radius: 8px !important;
}}
[data-baseweb="tag"] span {{ color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important; }}

/* ---------- BOTONES ---------- */
.stButton > button, .stFormSubmitButton > button {{
    background: {p['acento']};
    color: {p['texto_boton']};
    border: 0;
    border-radius: 12px;
    padding: 0.7rem 1.3rem;
    font-weight: 700;
    width: 100%;
    transition: transform .15s ease, filter .15s ease, box-shadow .15s ease;
}}
.stButton > button:hover, .stFormSubmitButton > button:hover {{
    filter: brightness(0.94);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,.14);
    color: {p['texto_boton']};
    border: 0;
}}
.stButton > button p, .stFormSubmitButton > button p {{
    color: {p['texto_boton']} !important; font-weight: 700;
}}
.stLinkButton a {{
    background: {p['primario']} !important;
    border: 0 !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    width: 100%;
    transition: transform .15s ease, box-shadow .15s ease;
}}
.stLinkButton a:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,.14);
}}
.stLinkButton a p {{
    color: {'#12271F' if p['primario'] == '#D9A93F' else '#FFFFFF'} !important;
    font-weight: 700 !important;
}}

/* ---------- TARJETAS ---------- */
.tarjeta {{
    background: {p['tarjeta']};
    border: 1px solid {p['borde']};
    border-top: 3px solid {p['detalle']};
    border-radius: 16px;
    padding: 18px 20px;
    height: 100%;
    box-shadow: 0 1px 3px rgba(0,0,0,.05);
    transition: transform .18s ease, box-shadow .18s ease;
}}
.tarjeta:hover {{
    transform: translateY(-4px);
    box-shadow: 0 10px 24px rgba(0,0,0,.10);
}}
.tarjeta h4 {{ margin: 0 0 .4rem 0; font-size: 1rem; color: {p['primario']}; }}
.tarjeta p {{ margin: 0; color: {p['suave']}; font-size: .92rem; line-height: 1.45; }}

/* ---------- BARRA FIJA DE MARCA ---------- */
.barra-marca {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 72px;
    background: {p['fondo']};
    border-bottom: 2px solid {p['detalle']};
    box-shadow: 0 2px 14px rgba(0,0,0,.08);
    display: flex; align-items: center;
    padding: 0 28px;
    z-index: 999;
    backdrop-filter: blur(6px);
}}
.barra-marca img {{ height: 46px; width: auto; }}
@media (max-width: 640px) {{
    .barra-marca {{ height: 60px; padding: 0 16px; }}
    .barra-marca img {{ height: 36px; }}
}}

/* ---------- FOTO DEL ASESOR ---------- */
.foto-asesor {{
    border-radius: 50%;
    border: 3px solid {p['detalle']};
    background: {p['tarjeta']};
    box-shadow: 0 4px 14px rgba(0,0,0,.12);
}}

/* ---------- LOGO ---------- */
.logo img {{ max-width: 260px; height: auto; }}
[data-testid="stImage"] img {{ border-radius: 0; }}

/* ---------- CABECERA DEL ASESOR ---------- */
.asesor-nombre {{
    font-size: 1.15rem; font-weight: 700; color: {p['texto']};
    margin: .15rem 0 .1rem 0;
}}
.asesor-claim {{ color: {p['suave']}; font-size: .93rem; margin: 0; }}
.avatar {{
    width: 104px; height: 104px; border-radius: 50%;
    background: {p['tarjeta']}; border: 2px solid {p['detalle']};
    display: flex; align-items: center; justify-content: center; font-size: 2.6rem;
}}

/* ---------- SELLOS DE CONFIANZA ---------- */
.sello {{
    display: inline-block;
    background: {p['tarjeta']};
    border: 1px solid {p['borde']};
    border-left: 3px solid {p['detalle']};
    border-radius: 999px;
    padding: 7px 14px; margin: 3px 6px 3px 0;
    font-size: .85rem; color: {p['suave']};
    transition: transform .15s ease;
}}
.sello:hover {{ transform: translateY(-2px); }}

/* ---------- MÉTRICAS, AVISOS Y PROGRESO ---------- */
[data-testid="stMetric"] {{
    background: {p['tarjeta']};
    border: 1px solid {p['borde']};
    border-left: 4px solid {p['detalle']};
    border-radius: 14px; padding: 14px 18px;
}}
[data-testid="stMetricValue"] {{ color: {p['primario']}; font-weight: 700; }}
[data-testid="stMetricLabel"] p {{ color: {p['suave']} !important; }}
.stProgress > div > div > div > div {{
    background-color: {p['detalle']};
    transition: width .6s ease;
}}
[data-testid="stAlertContainer"] {{
    background: {p['tarjeta']};
    border: 1px solid {p['borde']};
    border-radius: 12px;
}}
[data-testid="stAlertContainer"] p {{ color: {p['texto']}; }}
[data-testid="stExpander"] details {{
    background: {p['tarjeta']};
    border: 1px solid {p['borde']};
    border-radius: 12px;
}}

/* ---------- MÓVIL ---------- */
@media (max-width: 640px) {{
    h1 {{ font-size: 1.65rem !important; }}
    .block-container {{ padding-left: 1rem; padding-right: 1rem; }}
    .stApp::before {{ display: none; }}
}}
</style>
"""
