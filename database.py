import sqlite3
import json
from datetime import datetime

DB_PATH = "contactos.db"


def ahora():
    """Devuelve la fecha y hora actual como texto."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def crear_tabla():
    """Crea las tablas 'contactos' y 'candidatos' si no existen."""
    conn = sqlite3.connect(DB_PATH)

    # Tabla de clientes que quieren ahorrar
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

    # Tabla de personas que quieren unirse al equipo
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

    conn.commit()
    conn.close()


def guardar_contacto(nombre, telefono, email, ciudad, horario, pagos, consentimiento):
    """Guarda un cliente interesado en ahorrar."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO contactos
        (fecha, nombre, telefono, email, ciudad, horario,
         servicios, gasto_mensual, consentimiento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ahora(), nombre, telefono, email, ciudad, horario,
            json.dumps(pagos, ensure_ascii=False),
            sum(pagos.values()),
            int(consentimiento),
        ),
    )
    conn.commit()
    conn.close()


def guardar_candidato(nombre, telefono, email, ciudad, situacion,
                      experiencia, disponibilidad, mensaje, consentimiento):
    """Guarda una persona interesada en unirse al equipo."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO candidatos
        (fecha, nombre, telefono, email, ciudad, situacion,
         experiencia, disponibilidad, mensaje, consentimiento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ahora(), nombre, telefono, email, ciudad, situacion,
            experiencia, disponibilidad, mensaje, int(consentimiento),
        ),
    )
    conn.commit()
    conn.close()