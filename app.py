import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# CONFIGURACIÓN
# ==========================================
st.set_page_config(
    page_title="Dashboard Analítico Personalizado",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Analítico Personalizado")
st.subheader("Caso de Estudio: Abandono de Clientes (Churn)")
st.markdown("---")

# ==========================================
# CARGAR DATASET
# ==========================================
@st.cache_data
def cargar_datos():
    return pd.read_csv("dataset_personal.csv")

df = cargar_datos()

# ==========================================
# KPI
# ==========================================
st.header("📌 Visualización 1: Indicador KPI")

tasa_churn = df["Churn"].mean() * 100

st.metric(
    label="Tasa de Churn",
    value=f"{tasa_churn:.2f}%"
)

st.markdown("---")

# ==========================================
# BARRAS
# ==========================================
st.header("📊 Visualización 2: Gráfico de Barras")

fig1, ax1 = plt.subplots(figsize=(6,4))

sns.countplot(
    data=df,
    x="Tipo_Contrato",
    palette="Set2",
    ax=ax1
)

ax1.set_title("Clientes por Tipo de Contrato")
ax1.set_xlabel("Tipo de Contrato")
ax1.set_ylabel("Cantidad")

st.pyplot(fig1)

st.markdown("---")

# ==========================================
# HISTOGRAMA
# ==========================================
st.header("📈 Visualización 3: Histograma")

fig2, ax2 = plt.subplots(figsize=(6,4))

ax2.hist(
    df["Pago_Mensual"],
    bins=20,
    color="skyblue",
    edgecolor="black"
)

ax2.set_title("Distribución del Pago Mensual")
ax2.set_xlabel("Pago Mensual")
ax2.set_ylabel("Frecuencia")

st.pyplot(fig2)

st.markdown("---")

# ==========================================
# SCATTER
# ==========================================
st.header("🎯 Visualización 4: Scatter Plot")

fig3, ax3 = plt.subplots(figsize=(6,4))

sns.scatterplot(
    data=df,
    x="Meses_Contrato",
    y="Pago_Mensual",
    hue="Churn",
    palette="Set1",
    ax=ax3
)

ax3.set_title("Meses de Contrato vs Pago Mensual")
ax3.set_xlabel("Meses de Contrato")
ax3.set_ylabel("Pago Mensual")

st.pyplot(fig3)

st.markdown("---")

# ==========================================
# STORYTELLING
# ==========================================
st.header("📖 Storytelling de Datos")

st.subheader("Hallazgos principales")

st.markdown("""
- **Hallazgo 1:** Los clientes con contratos **Mes a mes** presentan la mayor tasa de abandono.

- **Hallazgo 2:** Los clientes con mayor número de reclamos muestran una mayor probabilidad de abandonar el servicio.

- **Hallazgo 3:** Los clientes con mayor antigüedad tienen una menor tasa de churn, lo que indica una mayor fidelización.
""")

st.subheader("Recomendaciones")

st.markdown("""
- **Recomendación 1:** Implementar campañas de fidelización para clientes con contratos mensuales.

- **Recomendación 2:** Mejorar el servicio de atención al cliente para reducir la cantidad de reclamos.

- **Recomendación 3:** Aplicar modelos predictivos para identificar clientes con alto riesgo de abandono.
""")

# ==========================================
# TABLA DE DATOS
# ==========================================
st.markdown("---")
st.header("📋 Vista previa del Dataset")

st.dataframe(df.head(10), use_container_width=True)
