import streamlit as st
import pandas as pd

# ====================================================
# CONFIGURACIÓN INICIAL DE LA INTERFAZ WEB
# ====================================================
st.set_page_config(
    page_title="Dashboard BI - KPI Principal",
    page_icon="📊",
    layout="wide"
)

# Títulos principales de la aplicación según la guía de laboratorio
st.title("📊 Dashboard Analítico Personalizado")
st.markdown("### Caso de Estudio: Abandono de Clientes (Churn / Deserción)")
st.markdown("---")

# ====================================================
# CARGA SEGURA DEL DATASET PERSONALIZADO
# ====================================================
@st.cache_data
def cargar_datos():
    try:
        # Intenta leer el archivo .csv generado en la Actividad 1
        return pd.read_csv("dataset_personal.csv")
    except FileNotFoundError:
        st.error("⚠️ Error: No se encontró el archivo 'dataset_personal.csv'. Asegúrate de haber ejecutado la Actividad 1.")
        return None

df = cargar_datos()

if df is not None:
    # ====================================================
    # RESTRICCIÓN OBLIGATORIA - VISUALIZACIÓN 1: INDICADOR KPI
    # ====================================================
    st.subheader("📌 Visualización 1: Indicador KPI Organizacional")
    
    # Calcular matemáticamente la tasa real basada en tus datos únicos (promedio de la columna objetivo)
    tasa_desercion = df['Churn'].mean() * 100
    
    # Renderizar la tarjeta de métrica nativa y profesional de Streamlit
    st.metric(
        label="Tasa de Deserción General (Churn Rate)", 
        value=f"{tasa_desercion:.2f}%",
        delta="Métrica de Control Crítica"
    )
    
    st.markdown("---")
