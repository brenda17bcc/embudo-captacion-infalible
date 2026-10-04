"""Base de datos del embudo: clientes de ahorro, candidatos e inmuebles."""

import sqlite3
import json
from datetime import datetime

DB_PATH = "contactos.db"


def ahora():
    """Devuelve la fecha y hora actual como texto."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def columna_si_falta(conn, tabla, columna, tipo="TEXT"):
    """Añade una columna a una tabla solo si todavía no existe (migración)."""
    columnas = [fila[1] for fila in conn.execute(f"PRAGMA table_info({tabla})")]
    if columna not in columnas:
        conn.execute(f"ALTER TABLE {tabla} ADD COLUMN {columna} {tipo}")


def crear_tabla():
    """Crea las tablas si no existen y las actualiza si falta alguna columna."""
    conn = sqlite3.connect(DB_PATH)

    # 1. Clientes que quieren ahorrar en sus servicios
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT,
            ciudad TEXT,
            horario TEXT,
            servicios TEXT NOT NULL,
            gasto_mensual REAL,
            consentimiento INTEGER NOT NULL,
            estado TEXT DEFAULT 'Nuevo'
        )
    """)

    # 2. Personas que quieren unirse al equipo
    conn.execute("""
        CREATE TABLE IF NOT EXISTS candidatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT,
            ciudad TEXT,
            situacion TEXT,
            experiencia TEXT,
            disponibilidad TEXT,
            mensaje TEXT,
            consentimiento INTEGER NOT NULL,
            estado TEXT DEFAULT 'Nuevo'
        )
    """)

    # 3. Personas que quieren comprar, vender o alquilar una vivienda
    conn.execute("""
        CREATE TABLE IF NOT EXISTS inmuebles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT,
            zona TEXT,
            operacion TEXT NOT NULL,
            tipo TEXT,
            habitaciones INTEGER,
            importe REAL,
            plazo TEXT,
            financiacion TEXT,
            consentimiento INTEGER NOT NULL,
            idioma TEXT,
            detalles TEXT,
            estado TEXT DEFAULT 'Nuevo'
        )
    """)

    columna_si_falta(conn, "contactos", "idioma")
    columna_si_falta(conn, "inmuebles", "detalles")
    columna_si_falta(conn, "candidatos", "idioma")

    conn.commit()
    conn.close()


def guardar_contacto(nombre, telefono, email, ciudad, horario,
                     pagos, consentimiento, idioma="es"):
    """Guarda un cliente interesado en ahorrar."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO contactos
        (fecha, nombre, telefono, email, ciudad, horario,
         servicios, gasto_mensual, consentimiento, idioma)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ahora(), nombre, telefono, email, ciudad, horario,
            json.dumps(pagos, ensure_ascii=False),
            sum(pagos.values()),
            int(consentimiento),
            idioma,
        ),
    )
    conn.commit()
    conn.close()


def guardar_candidato(nombre, telefono, email, ciudad, situacion,
                      experiencia, disponibilidad, mensaje,
                      consentimiento, idioma="es"):
    """Guarda una persona interesada en unirse al equipo."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO candidatos
        (fecha, nombre, telefono, email, ciudad, situacion,
         experiencia, disponibilidad, mensaje, consentimiento, idioma)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ahora(), nombre, telefono, email, ciudad, situacion,
            experiencia, disponibilidad, mensaje,
            int(consentimiento), idioma,
        ),
    )
    conn.commit()
    conn.close()


def guardar_inmueble(nombre, telefono, email, zona, operacion, tipo,
                     habitaciones, importe, plazo, financiacion,
                     consentimiento, idioma="es", detalles=None):
    """Guarda una persona interesada en comprar, vender, alquilar o colaborar.

    'detalles' es un diccionario con los datos propios de cada caso
    (duración del alquiler, mascotas, agencia colaboradora...). Se guarda
    en una sola columna en formato JSON, así podemos añadir preguntas
    nuevas sin tener que cambiar la base de datos cada vez.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO inmuebles
        (fecha, nombre, telefono, email, zona, operacion, tipo,
         habitaciones, importe, plazo, financiacion, consentimiento,
         idioma, detalles)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ahora(), nombre, telefono, email, zona, operacion, tipo,
            habitaciones, importe, plazo, financiacion,
            int(consentimiento), idioma,
            json.dumps(detalles or {}, ensure_ascii=False),
        ),
    )
    conn.commit()
    conn.close()
