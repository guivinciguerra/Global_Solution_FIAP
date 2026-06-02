import streamlit as st


def render_sidebar():

    st.sidebar.image(
        "assets/logo.png",
        width=180
    )

    st.sidebar.title(
        "FloodWatch AI"
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        "Monitoramento Inteligente de Enchentes"
    )