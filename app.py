import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Inditex Strategic Analysis",
    layout="wide"
)

# TÍTULO
st.title("Inditex Strategic Analysis (2017–2025)")
st.subheader("From Fast Fashion Giant to Premium-Digital Retail Model")

# CARGAR DATOS
df = pd.read_excel("Inditex.xlsx")

# MOSTRAR DATASET
st.header("Dataset Overview")
st.dataframe(df)

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Ventas 2025",
        value=f"€{df['Ventas_Billones_EUR'].iloc[-1]}B"
    )

with col2:
    st.metric(
        label="Tiendas 2025",
        value=int(df['Tiendas'].iloc[-1])
    )

with col3:
    st.metric(
        label="Online % 2025",
        value=f"{df['Online_%'].iloc[-1]}%"
    )

# GRÁFICA DE VENTAS
st.header("Revenue Growth")

fig = px.line(
    df,
    x="Año",
    y="Ventas_Billones_EUR",
    markers=True,
    title="Inditex Revenue Evolution"
)

st.plotly_chart(fig, use_container_width=True)

# GRÁFICA DE TIENDAS
st.header("Store Reduction Strategy")

fig2 = px.line(
    df,
    x="Año",
    y="Tiendas",
    markers=True,
    title="Number of Stores Over Time"
)

st.plotly_chart(fig2, use_container_width=True)

# TEXTO ESTRATÉGICO
st.header("Strategic Insight")

st.write("""
Inditex experienced a major transformation between 2017 and 2025.
While the company reduced its physical store count significantly,
revenues and profitability continued to grow.

This suggests a transition from a traditional fast fashion model
toward a more digital, efficient and premium-oriented retail strategy.
""")
