import streamlit as st
from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades
from src.utils.constantes import ORDEM_RISCO
from dashboard.components.cards import card_alerta


def render():
    st.markdown("## Central de Alertas")
    st.markdown(
        "<p style='color:#64748b;margin-top:-0.5rem;margin-bottom:1.5rem;font-size:0.9rem;'>"
        "Regiões classificadas em nível de risco alto ou crítico."
        "</p>",
        unsafe_allow_html=True,
    )

    df = carregar_simulacao()
    df = analisar_cidades(df)

    alertas = df[df["risco"].isin(["ALTO", "CRÍTICO"])].copy()
    alertas["risco_ordem"] = alertas["risco"].map(
        {r: i for i, r in enumerate(ORDEM_RISCO)}
    )
    alertas = alertas.sort_values("risco_ordem")

    if alertas.empty:
        st.success(
            "Nenhuma região em situação de alerta no momento. "
            "Todas as áreas operam dentro dos parâmetros normais.",
            icon="✅",
        )
        return

    criticos = alertas[alertas["risco"] == "CRÍTICO"]
    altos = alertas[alertas["risco"] == "ALTO"]

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total de Alertas", len(alertas))
    with m2:
        st.metric("🔴 Críticos", len(criticos))
    with m3:
        st.metric("🟠 Altos", len(altos))

    st.markdown("<hr style='margin:1.2rem 0;border:none;border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)

    if not criticos.empty:
        st.markdown("### 🔴 Situações Críticas")
        col1, col2 = st.columns(2)
        for i, (_, row) in enumerate(criticos.iterrows()):
            with col1 if i % 2 == 0 else col2:
                card_alerta(
                    cidade=row["cidade"],
                    risco=row["risco"],
                    chuva=row["chuva"],
                    nivel_rio=row["nivel_rio"],
                )

    if not altos.empty:
        st.markdown("### 🟠 Alertas em Nível Alto")
        col1, col2 = st.columns(2)
        for i, (_, row) in enumerate(altos.iterrows()):
            with col1 if i % 2 == 0 else col2:
                card_alerta(
                    cidade=row["cidade"],
                    risco=row["risco"],
                    chuva=row["chuva"],
                    nivel_rio=row["nivel_rio"],
                )
