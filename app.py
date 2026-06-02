from dashboard.components.sidebar import render_sidebar
import streamlit as st

from dashboard.pages import (
    home,
    monitoramento,
    alertas,
    relatorios,
    mapa_risco,
    ia_assistente
)

st.set_page_config(
    page_title="FloodWatch AI",
    layout="wide"
)

render_sidebar()

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Mapa de Risco",
        "Dashboard",
        "Monitoramento",
        "Alertas",
        "Relatórios",
        "IA Assistente"
    ]
)

if pagina == "Dashboard":
    home.render()

elif pagina == "Monitoramento":
    monitoramento.render()

elif pagina == "Mapa de Risco":
    mapa_risco.render()

elif pagina == "IA Assistente":
    ia_assistente.render()

elif pagina == "Alertas":
    alertas.render()

elif pagina == "Relatórios":
    relatorios.render()