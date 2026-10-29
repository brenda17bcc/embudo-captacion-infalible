"""Herramienta rápida para revisar lo guardado, desde el CMD."""

import database

database.crear_tabla()
print("Guardando en:", database.donde_guarda(), "\n")

for titulo, tabla, campos in [
    ("CLIENTES DE AHORRO", "contactos",
     ["id", "fecha", "nombre", "telefono", "gasto_mensual", "idioma", "estado"]),
    ("CANDIDATOS AL EQUIPO", "candidatos",
     ["id", "fecha", "nombre", "telefono", "situacion", "idioma", "estado"]),
    ("VIVIENDA: COMPRA / VENTA / ALQUILER", "inmuebles",
     ["id", "fecha", "nombre", "telefono", "operacion", "zona", "idioma", "estado"]),
]:
    filas = database.leer_tabla(tabla)
    print(f"=== {titulo} ({len(filas)}) ===")
    for fila in filas:
        print(" | ".join(str(fila.get(c, "")) for c in campos))
    print()
