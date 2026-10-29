"""Base de datos del embudo.

Funciona de dos maneras, sin cambiar nada más:

* En tu ordenador, si no hay configurada una base de datos en la nube,
  guarda en el archivo local `contactos.db` (SQLite), como hasta ahora.
* En internet, si existe `url_base_datos` en los secretos, guarda en
  PostgreSQL (Neon), que no se borra nunca.

Tablas: contactos (ahorro), candidatos (equipo) e inmuebles (vivienda).
"""

import json
import os
from datetime import datetime

DB_PATH = "contactos.db"


# ---------------------------------------------------------------
# ¿Dónde guardamos? Nube si hay cadena de conexión; si no, local
# ---------------------------------------------------------------
def _url_nube():
    """Busca la cadena de conexión en las variables de entorno,
    en los secretos de Streamlit o en el archivo local de secretos."""
    url = os.environ.get("URL_BASE_DATOS", "")
    if url:
        return url

    try:
        import streamlit as st
        url = st.secrets.get("url_base_datos", "")
        if url:
            return url
    except Exception:
        pass

    ruta = os.path.join(".streamlit", "secrets.toml")
    if os.path.exists(ruta):
        try:
            import tomllib
            with open(ruta, "rb") as archivo:
                return tomllib.load(archivo).get("url_base_datos", "")
        except Exception:
            pass
    return ""


URL_NUBE = _url_nube()
EN_LA_NUBE = bool(URL_NUBE)

# Si la conexión tarda demasiado, que avise en vez de quedarse colgada
if EN_LA_NUBE and "connect_timeout" not in URL_NUBE:
    URL_NUBE += ("&" if "?" in URL_NUBE else "?") + "connect_timeout=30"

# Las tablas solo se comprueban una vez por sesión
_tablas_listas = False


def conexion():
    """Abre una conexión a la base de datos que toque."""
    if EN_LA_NUBE:
        import psycopg
        return psycopg.connect(URL_NUBE)
    import sqlite3
    return sqlite3.connect(DB_PATH)


def consulta(sql):
    """Adapta la consulta al tipo de base de datos.

    SQLite usa '?' para los huecos y PostgreSQL usa '%s'.
    Escribimos siempre con '?' y aquí se traduce si hace falta.
    """
    return sql.replace("?", "%s") if EN_LA_NUBE else sql


def ahora():
    """Devuelve la fecha y hora actual como texto."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# ---------------------------------------------------------------
# Creación de las tablas
# ---------------------------------------------------------------
def _tipo_id():
    return "SERIAL PRIMARY KEY" if EN_LA_NUBE else "INTEGER PRIMARY KEY AUTOINCREMENT"


def _tipo_decimal():
    return "DOUBLE PRECISION" if EN_LA_NUBE else "REAL"


def columna_si_falta(conn, tabla, columna, tipo="TEXT"):
    """Añade una columna solo si todavía no existe (migración segura)."""
    if EN_LA_NUBE:
        conn.execute(f"ALTER TABLE {tabla} ADD COLUMN IF NOT EXISTS {columna} {tipo}")
        return
    columnas = [fila[1] for fila in conn.execute(f"PRAGMA table_info({tabla})")]
    if columna not in columnas:
        conn.execute(f"ALTER TABLE {tabla} ADD COLUMN {columna} {tipo}")


def asegurar_tablas():
    """Comprueba las tablas solo la primera vez que hace falta.

    Así la página carga rápido: la base de datos de la nube solo se toca
    cuando alguien envía un formulario o se abre el panel.
    """
    global _tablas_listas
    if not _tablas_listas:
        crear_tabla()
        _tablas_listas = True


def crear_tabla():
    """Crea las tablas si no existen y añade las columnas que falten."""
    global _tablas_listas
    conn = conexion()
    id_col, decimal = _tipo_id(), _tipo_decimal()

    # 1. Clientes que quieren ahorrar en sus servicios
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS contactos (
            id {id_col},
            fecha TEXT NOT NULL,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT,
            ciudad TEXT,
            horario TEXT,
            servicios TEXT NOT NULL,
            gasto_mensual {decimal},
            consentimiento INTEGER NOT NULL,
            estado TEXT DEFAULT 'Nuevo'
        )
    """)

    # 2. Personas que quieren unirse al equipo
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS candidatos (
            id {id_col},
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

    # 3. Vivienda: comprar, vender, alquilar o colaborar
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS inmuebles (
            id {id_col},
            fecha TEXT NOT NULL,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT,
            zona TEXT,
            operacion TEXT NOT NULL,
            tipo TEXT,
            habitaciones INTEGER,
            importe {decimal},
            plazo TEXT,
            financiacion TEXT,
            consentimiento INTEGER NOT NULL,
            idioma TEXT,
            detalles TEXT,
            estado TEXT DEFAULT 'Nuevo'
        )
    """)

    columna_si_falta(conn, "contactos", "idioma")
    columna_si_falta(conn, "contactos", "companias")
    columna_si_falta(conn, "candidatos", "idioma")
    columna_si_falta(conn, "inmuebles", "detalles")

    conn.commit()
    conn.close()
    _tablas_listas = True


# ---------------------------------------------------------------
# Guardado de contactos
# ---------------------------------------------------------------
def guardar_contacto(nombre, telefono, email, ciudad, horario,
                     pagos, consentimiento, idioma="es", companias=None):
    """Guarda un cliente interesado en ahorrar.

    'companias' es un diccionario {servicio: compañía actual}, muy útil para
    que el asesor sepa de dónde viene cada contacto antes de llamar.
    """
    asegurar_tablas()
    conn = conexion()
    conn.execute(
        consulta("""
        INSERT INTO contactos
        (fecha, nombre, telefono, email, ciudad, horario,
         servicios, gasto_mensual, consentimiento, idioma, companias)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """),
        (
            ahora(), nombre, telefono, email, ciudad, horario,
            json.dumps(pagos, ensure_ascii=False),
            sum(pagos.values()),
            int(consentimiento),
            idioma,
            json.dumps(companias or {}, ensure_ascii=False),
        ),
    )
    conn.commit()
    conn.close()


def guardar_candidato(nombre, telefono, email, ciudad, situacion,
                      experiencia, disponibilidad, mensaje,
                      consentimiento, idioma="es"):
    """Guarda una persona interesada en unirse al equipo."""
    asegurar_tablas()
    conn = conexion()
    conn.execute(
        consulta("""
        INSERT INTO candidatos
        (fecha, nombre, telefono, email, ciudad, situacion,
         experiencia, disponibilidad, mensaje, consentimiento, idioma)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """),
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

    'detalles' recoge en formato JSON lo propio de cada caso (duración del
    alquiler, mascotas, agencia colaboradora...), así se pueden añadir
    preguntas nuevas sin tener que cambiar la base de datos.
    """
    asegurar_tablas()
    conn = conexion()
    conn.execute(
        consulta("""
        INSERT INTO inmuebles
        (fecha, nombre, telefono, email, zona, operacion, tipo,
         habitaciones, importe, plazo, financiacion, consentimiento,
         idioma, detalles)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """),
        (
            ahora(), nombre, telefono, email, zona, operacion, tipo,
            habitaciones, importe, plazo, financiacion,
            int(consentimiento), idioma,
            json.dumps(detalles or {}, ensure_ascii=False),
        ),
    )
    conn.commit()
    conn.close()


# ---------------------------------------------------------------
# Lectura y actualización (las usa el panel privado)
# ---------------------------------------------------------------
def leer_tabla(nombre):
    """Devuelve todas las filas de una tabla como lista de diccionarios."""
    asegurar_tablas()
    conn = conexion()
    try:
        cursor = conn.execute(f"SELECT * FROM {nombre} ORDER BY id DESC")
        columnas = [c[0] for c in cursor.description]
        filas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    except Exception:
        filas = []
    conn.close()
    return filas


def cambiar_estado(tabla, fila_id, estado):
    """Cambia el estado de un contacto (Nuevo, Contactado, Cliente...)."""
    conn = conexion()
    conn.execute(
        consulta(f"UPDATE {tabla} SET estado = ? WHERE id = ?"),
        (estado, fila_id),
    )
    conn.commit()
    conn.close()


def donde_guarda():
    """Texto informativo para el panel: dónde se están guardando los datos."""
    return "☁️ Base de datos en la nube" if EN_LA_NUBE else "💾 Archivo local (contactos.db)"
