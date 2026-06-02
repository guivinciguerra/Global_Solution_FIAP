import streamlit as st

from src.services.previsao import (
    gerar_previsao
)

from src.utils.graficos import (
    grafico_previsao
)


def render():

    st.title(
        "🔮 Previsão de Enchentes"
    )

    previsoes = gerar_previsao(
        85
    )

    st.plotly_chart(
        grafico_previsao(
            previsoes
        ),
        use_container_width=True
    )