import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Dashboard Analítico",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Analítico Personalizado")
st.subheader("Caso de Estudio: Abandono de Clientes (Churn)")

@st.cache_data
def cargar_datos():
    return pd.read_csv("dataset_personal.csv")

df = cargar_datos()

# ==========================
# VISUALIZACIÓN 1 - KPI
# ==========================
st.header("📌 Visualización 1: KPI")

kpi = df["Churn"].mean()*100

st.metric(
    label="Tasa de Churn",
    value=f"{kpi:.2f}%"
)

st.divider()

# ==========================
# VISUALIZACIÓN 2 - BARRAS
# ==========================
st.header("📊 Visualización 2: Barras")

fig1, ax1 = plt.subplots(figsize=(6,4))

sns.countplot(
    data=df,
    x="Tipo_Contrato",
    ax=ax1
)

ax1.set_title("Clientes por Tipo de Contrato")

st.pyplot(fig1)

st.divider()

# ==========================
# VISUALIZACIÓN 3 - HISTOGRAMA
# ==========================
st.header("📈 Visualización 3: Histograma")

fig2, ax2 = plt.subplots(figsize=(6,4))

ax2.hist(df["Pago_Mensual"], bins=20)

ax2.set_title("Distribución del Pago Mensual")

st.pyplot(fig2)

st.divider()

# ==========================
# VISUALIZACIÓN 4 - SCATTER
# ==========================
st.header("🎯 Visualización 4: Scatter Plot")

fig3, ax3 = plt.subplots(figsize=(6,4))

sns.scatterplot(
    data=df,
    x="Meses_Contrato",
    y="Pago_Mensual",
    hue="Churn",
    ax=ax3
)

ax3.set_title("Meses de Contrato vs Pago Mensual")

st.pyplot(fig3)

st.divider()

# ==========================
# STORYTELLING
# ==========================

st.header("📖 Storytelling de Datos")

st.subheader("Hallazgos principales")

st.write("• Los clientes con contrato 'Mes a mes' presentan mayor probabilidad de abandono.")

st.write("• Los clientes con mayor número de reclamos muestran mayor riesgo de churn.")

st.write("• Los clientes con más meses de permanencia tienen menor tasa de abandono.")

st.subheader("Recomendaciones")

st.write("• Implementar programas de fidelización para contratos mensuales.")

st.write("• Mejorar la atención al cliente para reducir los reclamos.")

st.write("• Aplicar modelos predictivos para detectar clientes con alto riesgo de abandono.")
