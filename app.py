import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Inditex Strategic Analysis",
    layout="wide"
)

# =========================
# TÍTULO PRINCIPAL
# =========================

st.title("Inditex Strategic Analysis (2017–2025)")
st.subheader("From Fast Fashion Giant to Premium-Digital Retail Model")

# =========================
# INTRODUCCIÓN
# =========================

st.markdown("""
## The Peak of Fast Fashion

Between 2017 and 2020, Inditex represented one of the most dominant fast fashion companies in the world.

Brands like Zara expanded aggressively through:
- rapid inventory rotation
- global physical expansion
- trend acceleration
- affordable fashion positioning

At the time, physical stores were one of the company's strongest competitive advantages.
""")

# =========================
# CARGAR DATOS
# =========================

df = pd.read_excel("Inditex.xlsx")

# =========================
# DATASET
# =========================

st.header("Dataset Overview")
st.dataframe(df)

# =========================
# KPIs
# =========================

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

# =========================
# CAMBIO DEL MERCADO
# =========================

st.markdown("""
## The Industry Shift

After 2020, global retail experienced major structural changes.

The rise of:
- e-commerce
- digital shopping ecosystems
- ultra-fast fashion competitors like Shein
- inflation and pricing pressure

forced traditional fashion retailers to rethink their business models.

Inditex responded by:
- reducing physical stores
- strengthening online operations
- improving operational efficiency
- repositioning itself toward a more premium image
""")

# =========================
# GRÁFICA DE VENTAS
# =========================

st.header("Revenue Growth")

fig = px.line(
    df,
    x="Año",
    y="Ventas_Billones_EUR",
    markers=True,
    title="Inditex Revenue Evolution"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# GRÁFICA DE TIENDAS
# =========================

st.header("Store Reduction Strategy")

fig2 = px.line(
    df,
    x="Año",
    y="Tiendas",
    markers=True,
    title="Number of Stores Over Time"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# DIGITAL TRANSFORMATION
# =========================

st.header("Digital Transformation")

fig3 = px.line(
    df,
    x="Año",
    y="Online_%",
    markers=True,
    title="Online Sales Penetration"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# RENTABILIDAD
# =========================

st.header("Profitability Evolution")

fig4 = px.line(
    df,
    x="Año",
    y="EBITDA",
    markers=True,
    title="EBITDA Growth Over Time"
)

st.plotly_chart(fig4, use_container_width=True)

# =========================
# INTERPRETACIÓN ESTRATÉGICA
# =========================

st.header("Strategic Interpretation")

st.write("""
Although Inditex reduced its global store count significantly between 2019 and 2025,
revenues, EBITDA and profitability continued growing.

This may suggest:
- stronger operational efficiency
- higher online monetization
- improved supply chain optimization
- reduced dependence on physical expansion

The company appears to be transitioning from a traditional fast fashion model
toward a more digital, efficient and premium-oriented retail strategy.
""")

# =========================
# PREGUNTA ESTRATÉGICA
# =========================

st.header("Is Inditex Still Fast Fashion?")

st.write("""
Historically, Inditex helped define the global fast fashion industry.

However, rising prices, premium-oriented branding and the reduction of physical stores
may indicate a repositioning toward a hybrid retail model:
- faster than luxury fashion
- but more expensive than ultra-fast fashion competitors like Shein

This creates an interesting competitive tension between:
- affordability
- digital convenience
- brand perception
- and consumer expectations.

Despite reducing stores worldwide, Inditex continues generating record revenues,
suggesting that relevance today may depend less on physical presence
and more on digital dominance and operational efficiency.
""")
