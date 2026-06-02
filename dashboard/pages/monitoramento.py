import streamlit as st

from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades


def render():

    st.title("📡 Monitoramento")

    df = carregar_simulacao()

    df = analisar_cidades(df)

    st.dataframe(
        df,
        use_container_width=True
    )