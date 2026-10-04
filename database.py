import sqlite3
import json
from datetime import datetime

DB_PATH = "contactos.db"


def ahora():
    """Devuelve la fecha y hora actual como texto."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def columna_si_falta(conn, tabla, columna, tipo="TEXT"):
    """Añade una columna a una tabla solo si todavía no existe.
    Esto se llama 'migración': cambia la estructura sin perder los datos."""
    columnas = [fila[1] for fila in conn.execute(f"PRAGMA table_info({tabla})")]
    if columna not in columnas:
        conn.execute(f"ALTER TABLE {tabla} ADD COLUMN {columna} {tipo}")


def crear_tabla():
    """Crea las tablas si no existen y las actualiza si les falta alguna columna."""
    conn = sqlite3.connect(DB_PATH)

    # Clientes que quieren ahorrar
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

    # Personas que quieren unirse al equipo
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

    # Columnas añadidas después (migración)
    columna_si_falta(conn, "contactos", "idioma")
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