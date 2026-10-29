"""Compañías más comunes por servicio y porcentajes de ahorro estimado.

⚠️ IMPORTANTE PARA JAVIER
Los porcentajes de AHORRO_ESTIMADO son PROVISIONALES: están puestos para que
la mecánica funcione. Antes de publicar la web hay que sustituirlos por los
que tú puedas justificar con tu experiencia real.

Formato: "clave_servicio": (mínimo, máximo) en tanto por uno.
Ejemplo: (0.10, 0.20) significa "entre un 10 % y un 20 % de ahorro".
Si pones (0, 0) en un servicio, la app no muestra estimación para ese servicio.

Los nombres de las compañías se usan solo para que la persona indique dónde
está contratada ahora. No se usan logos ni se sugiere relación con ellas.
"""

# ---------------------------------------------------------------
# PORCENTAJES DE AHORRO ESTIMADO (PROVISIONALES — REVISAR)
# ---------------------------------------------------------------
AHORRO_ESTIMADO = {
    "medico": (0.10, 0.20),
    "dental": (0.10, 0.25),
    "coche": (0.15, 0.30),
    "luz": (0.10, 0.20),
    "internet": (0.15, 0.30),
    "tv": (0.15, 0.30),
    "movil": (0.15, 0.30),
    "hipoteca": (0.05, 0.15),
}

# ---------------------------------------------------------------
# COMPAÑÍAS MÁS HABITUALES POR SERVICIO
# Puedes añadir o quitar nombres libremente.
# ---------------------------------------------------------------
COMPANIAS = {
    "medico": ["Sanitas", "Adeslas", "DKV", "Asisa", "Mapfre", "Cigna", "AXA"],
    "dental": ["Sanitas", "Adeslas", "DKV", "Asisa", "Vitaldent", "Caser"],
    "coche": ["Mapfre", "Mutua Madrileña", "Línea Directa", "Allianz", "AXA",
              "Zurich", "Pelayo", "Reale", "Verti"],
    "luz": ["Endesa", "Iberdrola", "Naturgy", "Repsol", "TotalEnergies",
            "EDP", "Holaluz", "Octopus Energy"],
    "internet": ["Movistar", "Vodafone", "Orange", "MásMóvil", "Digi",
                 "Yoigo", "Pepephone", "Lowi", "O2"],
    "tv": ["Movistar Plus+", "Orange TV", "Vodafone TV", "DAZN", "Netflix",
           "Prime Video", "HBO Max", "Disney+"],
    "movil": ["Movistar", "Vodafone", "Orange", "Yoigo", "Digi", "MásMóvil",
              "Pepephone", "Lowi", "O2", "Simyo"],
    "hipoteca": ["CaixaBank", "BBVA", "Santander", "Banco Sabadell", "ING",
                 "Bankinter", "Unicaja", "Abanca", "Kutxabank", "Openbank"],
}


def companias_de(clave, texto_otra, texto_no_se):
    """Devuelve la lista de compañías de un servicio más 'Otra' y 'No lo sé'."""
    return COMPANIAS.get(clave, []) + [texto_otra, texto_no_se]


def ahorro_de(clave, pago_mensual):
    """Calcula el ahorro anual estimado (mínimo y máximo) de un servicio."""
    minimo, maximo = AHORRO_ESTIMADO.get(clave, (0, 0))
    anual = pago_mensual * 12
    return anual * minimo, anual * maximo
