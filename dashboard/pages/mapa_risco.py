import streamlit as st
from dashboard.components.mapa import exibir_mapa


def render():
    st.markdown("## 🗺️ Mapa de Risco")
    st.markdown(
        "<p style='color:#64748b;margin-top:-0.5rem;margin-bottom:1.5rem;font-size:0.9rem;'>"
        "Monitoramento geográfico das regiões analisadas com classificação de risco."
        "</p>",
        unsafe_allow_html=True,
    )
    exibir_mapa()
