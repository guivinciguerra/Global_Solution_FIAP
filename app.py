import streamlit as st

from dashboard.components.sidebar import render_sidebar
from dashboard.pages import (
    home,
    monitoramento,
    alertas,
    relatorios,
    mapa_risco,
)

st.set_page_config(
    page_title="FloodWatch AI",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #0f1b2d;
    }
    [data-testid="stSidebar"] * {
        color: #e8eaf0 !important;
    }
    [data-testid="stSidebarNav"] { display: none; }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    h1 { font-size: 1.7rem !important; font-weight: 700 !important; }
    h2 { font-size: 1.25rem !important; font-weight: 600 !important; }
    h3 { font-size: 1.05rem !important; font-weight: 600 !important; }
    div[data-testid="metric-container"] {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem 1.25rem;
    }
    .stDataFrame { border-radius: 8px; overflow: hidden; }
</style>
""", unsafe_allow_html=True)

render_sidebar()

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Centro de Operações",
        "Monitoramento",
        "Alertas",
        "Relatórios",
        "Mapa de Risco",
    ],
    label_visibility="collapsed",
)

if pagina == "Centro de Operações":
    home.render()
elif pagina == "Monitoramento":
    monitoramento.render()
elif pagina == "Alertas":
    alertas.render()
elif pagina == "Relatórios":
    relatorios.render()
elif pagina == "Mapa de Risco":
    mapa_risco.render()
