import streamlit as st

from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades

from src.utils.graficos import (
    grafico_chuva,
    grafico_rio
)


def render():

    st.title("📊 Relatórios")

    df = carregar_simulacao()

    df = analisar_cidades(df)

    st.plotly_chart(
        grafico_chuva(df),
        use_container_width=True
    )

    st.plotly_chart(
        grafico_rio(df),
        use_container_width=True
    )