import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Análisis Estratégico de Inditex",
    layout="wide"
)

# =========================
# CUSTOM STYLE
# =========================

st.markdown("""
<style>

.stApp {
    background-color: #F5F1EB;
}

html, body, [class*="css"] {
    color: #2B2B2B;
}

h1, h2, h3 {
    color: #2B2B2B;
}

[data-testid="stMetricValue"] {
    color: #8C5E3C;
    font-size: 32px;
}

[data-testid="stMetricLabel"] {
    color: #5A5A5A;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO PRINCIPAL
# =========================

st.title("Análisis Estratégico de Inditex (2017–2025)")
st.subheader("De gigante del fast fashion a modelo premium-digital")

# =========================
# INTRODUCCIÓN
# =========================

st.markdown("""
## El auge del fast fashion

Entre 2017 y 2020, Inditex representó una de las compañías de fast fashion más dominantes del mundo.

Marcas como Zara expandieron agresivamente su presencia mediante:
- rotación rápida de inventario
- expansión física global
- aceleración de tendencias
- posicionamiento de moda accesible

En ese momento, las tiendas físicas representaban una de las principales ventajas competitivas de la compañía.
""")

# =========================
# CARGAR DATOS
# =========================

df = pd.read_excel("Inditex.xlsx")

# =========================
# DATASET
# =========================

st.header("Vista general del dataset")
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
        label="Ventas online 2025",
        value=f"{df['Online_%'].iloc[-1]}%"
    )

# =========================
# CAMBIO DEL MERCADO
# =========================

st.markdown("""
## Transformación de la industria

Después de 2020, el retail global experimentó cambios estructurales importantes.

El crecimiento de:
- e-commerce
- ecosistemas digitales de compra
- competidores ultra-fast fashion como Shein
- inflación y presión sobre precios

obligó a las empresas tradicionales de moda a replantear sus modelos de negocio.

Inditex respondió mediante:
- reducción de tiendas físicas
- fortalecimiento del canal online
- mejora de eficiencia operativa
- reposicionamiento hacia una imagen más premium
""")

# =========================
# GRÁFICA DE VENTAS
# =========================

st.header("Crecimiento de ingresos")

fig = px.line(
    df,
    x="Año",
    y="Ventas_Billones_EUR",
    markers=True,
    title="Evolución de ingresos de Inditex"
)

fig.update_traces(
    line=dict(color="#8C5E3C", width=4)
)

fig.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B")
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# GRÁFICA DE TIENDAS
# =========================

st.header("Estrategia de reducción de tiendas")

fig2 = px.line(
    df,
    x="Año",
    y="Tiendas",
    markers=True,
    title="Número de tiendas a través del tiempo"
)

fig2.update_traces(
    line=dict(color="#A67B5B", width=4)
)

fig2.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B")
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# TRANSFORMACIÓN DIGITAL
# =========================

st.header("Transformación digital")

fig3 = px.line(
    df,
    x="Año",
    y="Online_%",
    markers=True,
    title="Participación de ventas online"
)

fig3.update_traces(
    line=dict(color="#6B4F3B", width=4)
)

fig3.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B")
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# RENTABILIDAD
# =========================

st.header("Evolución de rentabilidad")

fig4 = px.line(
    df,
    x="Año",
    y="EBITDA",
    markers=True,
    title="Crecimiento del EBITDA"
)

fig4.update_traces(
    line=dict(color="#C08A5D", width=4)
)

fig4.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B")
)

st.plotly_chart(fig4, use_container_width=True)

# =========================
# INTERPRETACIÓN ESTRATÉGICA
# =========================

st.header("Interpretación estratégica")

st.write("""
Aunque Inditex redujo significativamente su número global de tiendas entre 2019 y 2025,
los ingresos, EBITDA y rentabilidad continuaron creciendo.

Esto podría sugerir:
- mayor eficiencia operativa
- mayor monetización digital
- optimización de cadena de suministro
- menor dependencia de expansión física

La compañía parece estar transitando desde un modelo tradicional de fast fashion
hacia una estrategia retail más digital, eficiente y orientada a segmentos premium.
""")

# =========================
# PREGUNTA ESTRATÉGICA
# =========================

st.header("¿Sigue siendo Inditex fast fashion?")

st.write("""
Históricamente, Inditex ayudó a definir la industria global del fast fashion.

Sin embargo, el aumento de precios, el branding más premium y la reducción de tiendas físicas
podrían indicar un reposicionamiento hacia un modelo híbrido:
- más rápido que el lujo tradicional
- pero más costoso que competidores ultra-fast fashion como Shein

Esto genera una tensión competitiva interesante entre:
- accesibilidad
- conveniencia digital
- percepción de marca
- expectativas del consumidor

A pesar de reducir tiendas a nivel mundial, Inditex continúa generando ingresos récord,
lo que podría indicar que la relevancia actual depende menos de presencia física
y más de dominio digital y eficiencia operativa.
""")
