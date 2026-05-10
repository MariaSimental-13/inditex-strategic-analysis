import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Inditex Strategic Analysis",
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

p {
    font-size: 18px;
    line-height: 1.8;
    color: #2B2B2B;
}

ul {
    font-size: 18px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# MAIN TITLE
# ============================================

st.title("Inditex: The Value Metamorphosis (2017–2025)")
st.subheader("From fast-fashion dominance to a premium-digital ecosystem")

st.caption(
    "Fashion Intelligence • Retail Transformation • Consumer Behavior Analysis"
)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================
# INTRODUCTION
# ============================================

st.markdown("""
## The Era of Logistical Hegemony

Between 2017 and 2020, Inditex didn't just dominate the market: it dictated the rules of global consumption.

During this period, flagship brands like Zara consolidated their leadership through an aggressive expansion strategy built on four critical pillars.

<p><strong>Precision Logistics</strong><br>
An inventory turnover model that transformed scarcity into desire.</p>

<p><strong>Physical Omnipresence</strong><br>
The strategic deployment of flagship stores across the world's most vital commercial arteries.</p>

<p><strong>Trend Democratization</strong><br>
The unprecedented ability to translate runway hype to the streets in record time.</p>

<p><strong>Aspirational Positioning</strong><br>
Accessible fashion backed by a visual narrative mirroring the luxury segment.</p>

At this point in its history, the capillarity of its physical stores constituted one of the most solid competitive barriers within the global fast-fashion industry.
""", unsafe_allow_html=True)

# ============================================
# LOAD DATA
# ============================================

df = pd.read_excel("Inditex.xlsx")

# ============================================
# DATASET OVERVIEW
# ============================================

st.divider()

st.header("Dataset Overview")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ============================================
# KPIs
# ============================================

st.divider()

st.header("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="2025 Revenue",
        value=f"€{df['Ventas_Billones_EUR'].iloc[-1]}B"
    )

with col2:
    st.metric(
        label="2025 Store Count",
        value=int(df['Tiendas'].iloc[-1])
    )

with col3:
    st.metric(
        label="2025 Online Sales Share",
        value=f"{df['Online_%'].iloc[-1]}%"
    )

# ============================================
# INDUSTRY TRANSFORMATION
# ============================================

st.divider()

st.markdown("""
# Industry Transformation: The Great Post-2020 Pivot

## From Retail Inertia to Digital Ecosystem Agility

Starting in 2020, the global retail landscape underwent an unprecedented structural shift.

The meteoric rise of new paradigms forced traditional players to question their very existence.

<p><strong>E-commerce Hegemony</strong><br>
The transition from a mere purchasing option to a lifestyle ecosystem.</p>

<p><strong>The Ultra-Fast Fashion Threat</strong><br>
The emergence of competitors like Shein, capable of operating at disruptive speeds and volumes.</p>

<p><strong>Macroeconomic Pressure</strong><br>
Persistent inflation that redefined profit margins and consumer behavior.</p>

Inditex’s response was not resistance, but evolution.

<p><strong>Physical Footprint Optimization</strong><br>
A strategic pruning of points of sale to prioritize quality over quantity.</p>

<p><strong>Omnichannel Shielding</strong><br>
Total integration between physical and digital stock.</p>

<p><strong>Ascent to the Premium Segment</strong><br>
A brand repositioning aimed at distancing itself from the commoditization of cheap fashion.</p>
""", unsafe_allow_html=True)

# ============================================
# REVENUE CHART
# ============================================

st.divider()

st.header("Revenue Growth")

fig = px.line(
    df,
    x="Año",
    y="Ventas_Billones_EUR",
    markers=True,
    title="Inditex Revenue Evolution"
)

fig.update_traces(
    line=dict(color="#8C5E3C", width=4)
)

fig.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="Year",
    yaxis_title="Revenue (Billions EUR)"
)

st.plotly_chart(fig, use_container_width=True)

# ============================================
# STORE COUNT CHART
# ============================================

st.divider()

st.header("Store Reduction Strategy")

fig2 = px.line(
    df,
    x="Año",
    y="Tiendas",
    markers=True,
    title="Number of Stores Over Time"
)

fig2.update_traces(
    line=dict(color="#A67B5B", width=4)
)

fig2.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="Year",
    yaxis_title="Stores"
)

st.plotly_chart(fig2, use_container_width=True)

# ============================================
# DIGITAL TRANSFORMATION CHART
# ============================================

st.divider()

st.header("Digital Transformation")

fig3 = px.line(
    df,
    x="Año",
    y="Online_%",
    markers=True,
    title="Online Sales Participation"
)

fig3.update_traces(
    line=dict(color="#6B4F3B", width=4)
)

fig3.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="Year",
    yaxis_title="Online %"
)

st.plotly_chart(fig3, use_container_width=True)

# ============================================
# PROFITABILITY CHART
# ============================================

st.divider()

st.header("Profitability Evolution")

fig4 = px.line(
    df,
    x="Año",
    y="EBITDA",
    markers=True,
    title="EBITDA Growth"
)

fig4.update_traces(
    line=dict(color="#C08A5D", width=4)
)

fig4.update_layout(
    plot_bgcolor="#F5F1EB",
    paper_bgcolor="#F5F1EB",
    font=dict(color="#2B2B2B"),
    title_font=dict(size=24),
    xaxis_title="Year",
    yaxis_title="EBITDA"
)

st.plotly_chart(fig4, use_container_width=True)

# ============================================
# STRATEGIC INTERPRETATION
# ============================================

st.divider()

st.markdown("""
# Strategic Interpretation: Less is More

## Decoupling Physical Presence from Financial Performance

Despite an aggressive reduction in its global store network between 2019 and 2025, key indicators — revenue, EBITDA, and profitability — continue showing upward momentum.

This phenomenon reveals a profound operational paradigm shift.

<p><strong>Digital Monetization</strong><br>
The algorithm now carries as much weight as the storefront.</p>

<p><strong>Supply Chain Efficiency</strong><br>
A shorter, more local, and highly reactive value chain.</p>

<p><strong>Brick-and-Mortar Independence</strong><br>
Growth is no longer proportional to square footage, but to brand relevance.</p>

The company appears to be transitioning from a traditional fast-fashion structure toward a more efficient, digital, and premium-oriented retail strategy.
""", unsafe_allow_html=True)

# ============================================
# FINAL STRATEGIC QUESTION
# ============================================

st.divider()

st.markdown("""
# Is Inditex Still Fast Fashion?

## The Search for a Hybrid Equilibrium

While Inditex was one of the architects of the fast-fashion concept, its identity today appears to be moving toward a hybrid territory within global retail.

Rising price points, more sophisticated branding, and the reduction of physical stores suggest a strategic repositioning.

- More agile than traditional luxury.
- More exclusive than low-cost ultra-fast fashion.

This transformation creates a new competitive tension where the battle is no longer fought solely on price, but on:

- Value perception
- Digital convenience
- Brand positioning
- Consumer loyalty

Structurally, Inditex appears to be moving away from selling volume and toward selling efficient prestige.
""", unsafe_allow_html=True)
