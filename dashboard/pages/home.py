import streamlit as st

from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades

from dashboard.components.cards import card_metrica


def render():

    st.title("🏠 Dashboard")

    df = carregar_simulacao()

    df = analisar_cidades(df)

    total_cidades = len(df)

    cidades_criticas = len(
        df[df["risco"] == "CRÍTICO"]
    )

    media_chuva = round(
        df["chuva"].mean(),
        1
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        card_metrica(
            "Cidades Monitoradas",
            total_cidades
        )

    with col2:
        card_metrica(
            "Risco Crítico",
            cidades_criticas
        )

    with col3:
        card_metrica(
            "Média de Chuva",
            f"{media_chuva} mm"
        )

    st.markdown("---")

    st.subheader(
        "Situação Atual"
    )

    st.dataframe(df)