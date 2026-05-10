import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================
# CONFIGURACIÓN DE PÁGINA
# ============================================

st.set_page_config(
    page_title="Análisis Estratégico de Inditex",
    layout="wide"
)

# ============================================
# CUSTOM STYLE
# ============================================

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

section.main > div {
    padding-top: 2rem;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
}

[data-testid="stMetricValue"] {
    color: #8C5E3C;
    font-size: 32px;
    font-weight: 700;
}

[data-testid="stMetricLabel"] {
    color: #5A5A5A;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# TÍTULO PRINCIPAL
# ============================================

st.title("Inditex: La Metamorfosis del Valor (2017–2025)")
st.subheader("Del dominio del fast fashion hacia un ecosistema premium-digital")

st.caption(
    "Fashion Intelligence • Retail Transformation • Consumer Behavior Analysis"
)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================
# INTRODUCCIÓN
# ============================================

st.markdown("""
## La era de la hegemonía logística

Entre 2017 y 2020, Inditex no solo dominó el mercado: dictó las reglas del consumo global.

Durante este periodo, marcas insignia como Zara consolidaron su liderazgo mediante una estrategia de expansión agresiva fundamentada en cuatro pilares críticos.

**Logística de precisión**  
Un modelo de rotación de inventario que transformó la escasez en deseo.

**Omnipresencia física**  
El despliegue de una red de flagships en las arterias comerciales más estratégicas del mundo.

**Democratización de la tendencia**  
La capacidad inédita de trasladar el hype de las pasarelas al asfalto en tiempo récord.

**Posicionamiento aspiracional**  
Moda accesible respaldada por una narrativa visual cercana al lujo.

En este punto de su historia, la capilaridad de sus tiendas físicas constituía una de las barreras competitivas más sólidas dentro de la industria global del fast fashion.
""")

# ============================================
# CARGAR DATOS
# ============================================

df = pd.read_excel("Inditex.xlsx")

# ============================================
# DATASET
# ============================================

st.divider()

st.header("Vista general del dataset")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ============================================
# KPIs
# ============================================

st.divider()

st.header("Indicadores clave")

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

# ============================================
# TRANSFORMACIÓN INDUSTRIAL
# ============================================

st.divider()

st.markdown("""
# Transformación de la Industria: El Gran Pivot Post-2020

## De la inercia del retail a la agilidad del ecosistema digital

A partir de 2020, el tablero del retail global sufrió una sacudida estructural sin precedentes.

El ascenso meteórico de nuevos paradigmas obligó a los jugadores tradicionales a cuestionar su propia existencia.

**La hegemonía del E-commerce**  
El paso de una opción de compra a un ecosistema de vida.

**La amenaza del Ultra-Fast Fashion**  
El surgimiento de competidores como Shein, capaces de operar a velocidades y volúmenes disruptivos.

**Presión macroeconómica**  
Una inflación persistente que redefinió los márgenes de beneficio y el comportamiento del consumidor.

La respuesta de Inditex no fue la resistencia, sino la evolución.

**Optimización de huella física**  
Una poda estratégica de puntos de venta para priorizar calidad sobre cantidad.

**Blindaje omnicanal**  
La integración total entre stock físico y digital.

**Ascenso al segmento premium**  
Un reposicionamiento de marca que busca distanciarse de la comoditización de la moda barata.
""")

# ============================================
# GRÁFICA DE VENTAS
# ============================================

st.divider()

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
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="",
    yaxis_title=""
)

st.plotly_chart(fig, use_container_width=True)

# ============================================
# GRÁFICA DE TIENDAS
# ============================================

st.divider()

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
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="",
    yaxis_title=""
)

st.plotly_chart(fig2, use_container_width=True)

# ============================================
# TRANSFORMACIÓN DIGITAL
# ============================================

st.divider()

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
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="",
    yaxis_title=""
)

st.plotly_chart(fig3, use_container_width=True)

# ============================================
# RENTABILIDAD
# ============================================

st.divider()

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
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="",
    yaxis_title=""
)

st.plotly_chart(fig4, use_container_width=True)

# ============================================
# INTERPRETACIÓN ESTRATÉGICA
# ============================================

st.divider()

st.markdown("""
# Interpretación Estratégica: Menos es Más

## Desacoplamiento entre presencia física y rendimiento financiero

A pesar de una reducción agresiva en su red global de tiendas entre 2019 y 2025, los indicadores clave — ingresos, EBITDA y rentabilidad — muestran una tendencia ascendente.

Este fenómeno revela un cambio profundo de paradigma operativo.

**Monetización digital**  
El algoritmo ahora pesa tanto como el escaparate.

**Eficiencia de suministro**  
Una cadena de valor más corta, local y reactiva.

**Independencia del ladrillo**  
El crecimiento ya no es proporcional a los metros cuadrados, sino a la relevancia de marca.

La compañía parece estar transitando desde un modelo tradicional de fast fashion hacia una estrategia retail más eficiente, digital y orientada a segmentos premium.
""")

# ============================================
# PREGUNTA ESTRATÉGICA FINAL
# ============================================

st.divider()

st.markdown("""
# ¿Sigue siendo Inditex fast fashion?

## La búsqueda del equilibrio híbrido

Si bien Inditex fue uno de los arquitectos del concepto fast fashion, hoy su identidad parece desplazarse hacia un territorio intermedio dentro del retail global.

El incremento en precios, un branding más sofisticado y la reducción de tiendas físicas sugieren un modelo híbrido que busca posicionarse en un punto ciego para sus competidores.

- Más ágil que el lujo tradicional.
- Más exclusivo que el ultra-fast fashion de bajo coste.

Esta metamorfosis genera una tensión competitiva estratégica donde la batalla ya no se libra únicamente por precio, sino por:

- percepción de valor
- conveniencia digital
- posicionamiento de marca
- lealtad del consumidor

En términos estructurales, Inditex parece estar dejando de vender volumen para comenzar a vender prestigio eficiente.
""")
