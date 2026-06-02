from dashboard.components.sidebar import render_sidebar
import streamlit as st

from dashboard.pages import (
    home,
    monitoramento,
    alertas,
    relatorios
)

st.set_page_config(
    page_title="FloodWatch AI",
    layout="wide"
)

render_sidebar()

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Dashboard",
        "Monitoramento",
        "Alertas",
        "Relatórios"
    ]
)

if pagina == "Dashboard":
    home.render()

elif pagina == "Monitoramento":
    monitoramento.render()

elif pagina == "Alertas":
    alertas.render()

elif pagina == "Relatórios":
    relatorios.render()