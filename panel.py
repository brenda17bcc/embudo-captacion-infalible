"""Panel privado de Casa Criao.

Zona reservada para Javier: ver los contactos que entran por el embudo,
cambiar su estado y descargarlos. Protegido con contraseña.

Se arranca aparte de la web pública:
    streamlit run panel.py
"""

import json
import sqlite3
from io import BytesIO

import pandas as pd
import streamlit as st

import config
from estilos import obtener_paleta, css

DB_PATH = "contactos.db"
ESTADOS = ["Nuevo", "Contactado", "Propuesta enviada", "Cliente", "Descartado"]

# ---------- CONFIGURACIÓN ----------
st.set_page_config(
    page_title=f"Panel · {config.MARCA}",
    page_icon="📊",
    layout="wide",
)

paleta = obtener_paleta(config.PALETA)
st.markdown(css(paleta), unsafe_allow_html=True)

# El panel necesita toda la pantalla (la web pública va estrecha, el panel no)
st.markdown(
    """
    <style>
    .block-container {max-width: 100% !important; padding-top: 2.2rem !important;
                      padding-left: 2.5rem !important; padding-right: 2.5rem !important;}
    .stApp::before {display: none;}
    [data-testid="stDataFrame"], [data-testid="stDataEditor"] {width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- CONTRASEÑA ----------
def clave_guardada():
    """Lee la contraseña del archivo .streamlit/secrets.toml."""
    try:
        return st.secrets["clave_panel"]
    except Exception:
        return None


def pedir_clave():
    """Muestra la pantalla de acceso. Devuelve True si la clave es correcta."""
    if st.session_state.get("acceso_ok"):
        return True

    clave_real = clave_guardada()
    if not clave_real:
        st.error(
            "No hay contraseña configurada. Crea el archivo "
            "`.streamlit/secrets.toml` con la línea:  clave_panel = \"tu_clave\""
        )
        return False

    st.title("🔒 Panel privado")
    st.caption(f"{config.MARCA} · acceso reservado")
    clave = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        if clave == clave_real:
            st.session_state["acceso_ok"] = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta.")
    return False


# ---------- DATOS ----------
def leer_tabla(nombre):
    """Carga una tabla de la base de datos en una tabla de pandas."""
    conn = sqlite3.connect(DB_PATH)
    try:
        datos = pd.read_sql_query(f"SELECT * FROM {nombre} ORDER BY id DESC", conn)
    except Exception:
        datos = pd.DataFrame()
    conn.close()
    return datos


def guardar_estados(tabla, cambios):
    """Guarda en la base de datos los estados que se hayan modificado."""
    conn = sqlite3.connect(DB_PATH)
    for fila_id, estado in cambios:
        conn.execute(f"UPDATE {tabla} SET estado = ? WHERE id = ?", (estado, fila_id))
    conn.commit()
    conn.close()


def a_excel(hojas):
    """Convierte varias tablas en un único archivo Excel descargable."""
    memoria = BytesIO()
    with pd.ExcelWriter(memoria, engine="openpyxl") as escritor:
        for nombre, datos in hojas.items():
            datos.to_excel(escritor, sheet_name=nombre[:31], index=False)
    return memoria.getvalue()


def mostrar_tabla(titulo, tabla, datos, columnas_visibles):
    """Dibuja una pestaña del panel: filtros, tabla editable y descarga."""
    if datos.empty:
        st.info("Todavía no hay contactos en esta lista.")
        return

    # --- resumen ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", len(datos))
    col2.metric("Nuevos", int((datos["estado"] == "Nuevo").sum()))
    col3.metric("Clientes", int((datos["estado"] == "Cliente").sum()))

    # --- filtros ---
    col_f1, col_f2, col_f3 = st.columns([1, 1, 2])
    filtro_estado = col_f1.multiselect(
        "Estado", ESTADOS, key=f"estado_{tabla}", placeholder="Todos"
    )
    idiomas = sorted([i for i in datos.get("idioma", pd.Series()).dropna().unique()])
    filtro_idioma = col_f2.multiselect(
        "Idioma", idiomas, key=f"idioma_{tabla}", placeholder="Todos"
    )
    busqueda = col_f3.text_input(
        "Buscar por nombre o teléfono", key=f"buscar_{tabla}"
    )

    vista = datos.copy()
    if filtro_estado:
        vista = vista[vista["estado"].isin(filtro_estado)]
    if filtro_idioma:
        vista = vista[vista["idioma"].isin(filtro_idioma)]
    if busqueda.strip():
        texto = busqueda.strip().lower()
        vista = vista[
            vista["nombre"].str.lower().str.contains(texto, na=False)
            | vista["telefono"].str.lower().str.contains(texto, na=False)
        ]

    st.caption(f"Mostrando {len(vista)} de {len(datos)} contactos")

    # --- tabla editable (solo se puede cambiar el estado) ---
    columnas = [c for c in columnas_visibles if c in vista.columns]
    editada = st.data_editor(
        vista[columnas],
        key=f"editor_{tabla}",
        hide_index=True,
        use_container_width=True,
        disabled=[c for c in columnas if c != "estado"],
        column_config={
            "id": st.column_config.NumberColumn("Nº", width="small"),
            "fecha": st.column_config.TextColumn("Fecha", width="small"),
            "estado": st.column_config.SelectboxColumn(
                "Estado", options=ESTADOS, width="medium", required=True
            ),
        },
    )

    if st.button("💾 Guardar cambios de estado", key=f"guardar_{tabla}"):
        originales = dict(zip(vista["id"], vista["estado"]))
        cambios = [
            (int(fila_id), nuevo)
            for fila_id, nuevo in zip(editada["id"], editada["estado"])
            if originales.get(fila_id) != nuevo
        ]
        if cambios:
            guardar_estados(tabla, cambios)
            st.success(f"Guardados {len(cambios)} cambios.")
            st.rerun()
        else:
            st.info("No hay cambios que guardar.")

    # --- ficha completa de un contacto ---
    with st.expander("🔍 Ver la ficha completa de un contacto"):
        elegido = st.selectbox(
            "Elige el número de contacto",
            vista["id"].tolist(),
            key=f"ficha_{tabla}",
        )
        ficha = datos[datos["id"] == elegido].iloc[0].to_dict()
        for campo, valor in ficha.items():
            if valor in (None, "", "{}"):
                continue
            if campo == "detalles":
                st.markdown("**Detalles**")
                try:
                    for k, v in json.loads(valor).items():
                        if v not in (None, "", 0):
                            st.write(f"· {k.replace('_', ' ').capitalize()}: {v}")
                except Exception:
                    st.write(valor)
            elif campo == "servicios":
                st.markdown("**Servicios y gasto**")
                try:
                    for k, v in json.loads(valor).items():
                        st.write(f"· {k}: {v} €/mes")
                except Exception:
                    st.write(valor)
            else:
                st.write(f"**{campo.replace('_', ' ').capitalize()}:** {valor}")

    # --- descargas ---
    st.download_button(
        "⬇️ Descargar esta lista en CSV",
        vista.to_csv(index=False).encode("utf-8-sig"),
        file_name=f"{tabla}.csv",
        mime="text/csv",
        key=f"csv_{tabla}",
    )


# ---------- PANEL ----------
if pedir_clave():
    col_titulo, col_salir = st.columns([5, 1])
    with col_titulo:
        st.title(f"📊 Panel de {config.MARCA}")
        st.caption("Contactos recibidos desde el embudo")
    with col_salir:
        if st.button("Cerrar sesión"):
            st.session_state["acceso_ok"] = False
            st.rerun()

    contactos = leer_tabla("contactos")
    candidatos = leer_tabla("candidatos")
    inmuebles = leer_tabla("inmuebles")

    # descarga de todo en un Excel
    try:
        excel = a_excel({
            "Ahorro": contactos,
            "Equipo": candidatos,
            "Vivienda": inmuebles,
        })
        st.download_button(
            "📁 Descargar TODO en un Excel",
            excel,
            file_name="contactos_casa_criao.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    except Exception:
        st.caption(
            "Para descargar en Excel instala openpyxl:  pip install openpyxl  "
            "(mientras tanto puedes descargar cada lista en CSV)."
        )

    tab1, tab2, tab3 = st.tabs([
        f"💡 Ahorro ({len(contactos)})",
        f"🏡 Vivienda ({len(inmuebles)})",
        f"🤝 Equipo ({len(candidatos)})",
    ])

    with tab1:
        mostrar_tabla(
            "Ahorro", "contactos", contactos,
            ["id", "fecha", "nombre", "telefono", "email", "ciudad",
             "gasto_mensual", "horario", "idioma", "estado"],
        )

    with tab2:
        mostrar_tabla(
            "Vivienda", "inmuebles", inmuebles,
            ["id", "fecha", "nombre", "telefono", "email", "operacion",
             "tipo", "zona", "importe", "plazo", "idioma", "estado"],
        )

    with tab3:
        mostrar_tabla(
            "Equipo", "candidatos", candidatos,
            ["id", "fecha", "nombre", "telefono", "email", "ciudad",
             "situacion", "experiencia", "disponibilidad", "idioma", "estado"],
        )
