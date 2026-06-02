import streamlit as st
from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades
from src.utils.graficos import (
    grafico_chuva,
    grafico_rio,
    grafico_distribuicao_risco,
    grafico_historico,
    grafico_previsao,
)


def render():
    st.markdown("##  Relatórios Analíticos")
    st.markdown(
        "<p style='color:#64748b;margin-top:-0.5rem;margin-bottom:1.5rem;font-size:0.9rem;'>"
        "Visualização estatística das variáveis monitoradas e previsões de precipitação."
        "</p>",
        unsafe_allow_html=True,
    )

    df = carregar_simulacao()
    df = analisar_cidades(df)

    aba1, aba2, aba3 = st.tabs(["Dados Atuais", "Histórico", "Previsão"])

    with aba1:
        col_l, col_r = st.columns(2, gap="medium")
        with col_l:
            st.plotly_chart(grafico_chuva(df), use_container_width=True)
        with col_r:
            st.plotly_chart(grafico_rio(df), use_container_width=True)

        st.plotly_chart(grafico_distribuicao_risco(df), use_container_width=True)

    with aba2:
        fig_hist = grafico_historico()
        if fig_hist is not None:
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("Arquivo de histórico de chuvas não encontrado.")

    with aba3:
        st.markdown(
            "<p style='color:#64748b;font-size:0.85rem;margin-bottom:0.5rem;'>"
            "Estimativa baseada nos dados do sensor mais crítico e tendência de variação horária."
            "</p>",
            unsafe_allow_html=True,
        )
        st.plotly_chart(grafico_previsao(), use_container_width=True)
