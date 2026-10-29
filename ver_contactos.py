"""Herramienta para revisar lo que se ha guardado en la base de datos."""

import sqlite3

conn = sqlite3.connect("contactos.db")

clientes = conn.execute(
    "SELECT id, fecha, nombre, telefono, servicios, gasto_mensual, idioma, estado "
    "FROM contactos"
).fetchall()

candidatos = conn.execute(
    "SELECT id, fecha, nombre, telefono, situacion, disponibilidad, idioma, estado "
    "FROM candidatos"
).fetchall()

inmuebles = conn.execute(
    "SELECT id, fecha, nombre, telefono, operacion, tipo, zona, importe, "
    "idioma, estado FROM inmuebles"
).fetchall()

conn.close()

print(f"=== CLIENTES DE AHORRO ({len(clientes)}) ===")
for fila in clientes:
    print(fila)

print(f"\n=== CANDIDATOS AL EQUIPO ({len(candidatos)}) ===")
for fila in candidatos:
    print(fila)

print(f"\n=== VIVIENDA: COMPRA / VENTA / ALQUILER ({len(inmuebles)}) ===")
for fila in inmuebles:
    print(fila)
