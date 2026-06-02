import streamlit as st

from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades


def render():

    st.title("🚨 Alertas")

    df = carregar_simulacao()

    df = analisar_cidades(df)

    alertas = df[
        df["risco"].isin(
            ["ALTO", "CRÍTICO"]
        )
    ]

    if len(alertas) == 0:
        st.success(
            "Nenhum alerta encontrado."
        )

    else:

        for _, row in alertas.iterrows():

            st.warning(
                f"""
                Cidade: {row['cidade']}

                Risco: {row['risco']}

                Chuva: {row['chuva']} mm

                Nível do Rio: {row['nivel_rio']}%
                """
            )