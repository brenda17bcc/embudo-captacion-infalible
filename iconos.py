"""Iconos dibujados a medida para los servicios.

Son SVG propios (no imágenes descargadas): pesan muy poco, se ven nítidos
en cualquier pantalla y toman el color de la marca automáticamente.
"""

# Cada icono usa 'currentColor', así hereda el color que le pongamos por CSS
ICONOS = {
    "medico": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 21s-7-4.3-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.7-7 10-7 10z"/>
        <path d="M12 9.5v4M10 11.5h4"/></svg>""",

    "dental": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <path d="M7 3.8c1.6 0 2.2.9 5 .9s3.4-.9 5-.9c2 0 3 1.6 3 4 0 3-1 4.4-1.6 7.2
        -.5 2.4-.7 5-2.3 5s-1.5-3.7-2.6-5.6c-.4-.7-1.6-.7-2 0C10.4 16.3 10.5 20 9 20
        s-1.8-2.6-2.3-5C6 12.2 5 10.8 5 7.8c0-2.4 1-4 2-4z"/></svg>""",

    "coche": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 16v2.5M20 16v2.5M3 16h18v-3.2a2 2 0 0 0-.4-1.2L18.4 8.4
        A2 2 0 0 0 16.8 7.6H7.2a2 2 0 0 0-1.6.8L3.4 11.6A2 2 0 0 0 3 12.8z"/>
        <circle cx="7" cy="16" r="1.6"/><circle cx="17" cy="16" r="1.6"/></svg>""",

    "luz": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 18h6M10 21h4"/>
        <path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5.9 1.2.9 1.9v.2h5.2v-.2c0-.7.3-1.4.9-1.9
        A6 6 0 0 0 12 3z"/></svg>""",

    "internet": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <path d="M2.5 9a15 15 0 0 1 19 0M5.5 12.5a10 10 0 0 1 13 0M8.6 16a5.5 5.5 0 0 1 6.8 0"/>
        <circle cx="12" cy="19.3" r="1.1" fill="currentColor" stroke="none"/></svg>""",

    "tv": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <rect x="2.5" y="5" width="19" height="12" rx="2"/>
        <path d="M8 20h8M12 17v3"/></svg>""",

    "movil": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/>
        <path d="M10.5 5.5h3"/>
        <circle cx="12" cy="18" r="1" fill="currentColor" stroke="none"/></svg>""",

    "hipoteca": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3.5 10.5 12 3.5l8.5 7"/>
        <path d="M5.5 10v10h13V10"/>
        <path d="M10 17.5 14 13"/>
        <circle cx="10.2" cy="13.2" r="1"/><circle cx="13.8" cy="17.3" r="1"/></svg>""",
}


def icono(clave, tamano=34):
    """Devuelve el SVG del servicio, listo para insertar en la página."""
    svg = ICONOS.get(clave, "")
    if not svg:
        return ""
    return svg.replace(
        "<svg ", f'<svg width="{tamano}" height="{tamano}" ', 1
    )


def icono_css(clave, color):
    """Devuelve el icono listo para usarse como imagen de fondo en CSS."""
    from urllib.parse import quote
    svg = ICONOS.get(clave, "")
    if not svg:
        return ""
    svg = " ".join(svg.split())                    # todo en una línea
    svg = svg.replace("currentColor", color)
    svg = svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
    return "url(\"data:image/svg+xml,%s\")" % quote(svg, safe="")
