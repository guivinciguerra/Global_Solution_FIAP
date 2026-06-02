import streamlit as st
import pandas as pd
from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades
from src.utils.constantes import ORDEM_RISCO, COR_CRITICO, COR_ALTO, COR_MEDIO, COR_BAIXO


def _highlight_risco(val):
    mapa = {
        "CRÍTICO": f"color:{COR_CRITICO};font-weight:700;",
        "ALTO":    f"color:{COR_ALTO};font-weight:700;",
        "MÉDIO":   f"color:{COR_MEDIO};font-weight:600;",
        "BAIXO":   f"color:{COR_BAIXO};font-weight:600;",
    }
    return mapa.get(val, "")


def render():
    st.markdown("## Monitoramento Operacional")
    st.markdown(
        "<p style='color:#64748b;margin-top:-0.5rem;margin-bottom:1.5rem;font-size:0.9rem;'>"
        "Dados consolidados de todos os sensores e indicadores ambientais."
        "</p>",
        unsafe_allow_html=True,
    )

    df = carregar_simulacao()
    df = analisar_cidades(df)

    col_filtro, col_busca, col_btn = st.columns([2, 2, 1])

    with col_filtro:
        filtro_risco = st.multiselect(
            "Filtrar por risco",
            options=ORDEM_RISCO,
            default=ORDEM_RISCO,
            placeholder="Todos os níveis",
        )

    with col_busca:
        busca = st.text_input("Buscar cidade", placeholder="Digite o nome...")

    with col_btn:
        st.markdown("<div style='margin-top:1.75rem;'>", unsafe_allow_html=True)
        if st.button("🔄 Atualizar", use_container_width=True):
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    tabela = df.copy()
    if filtro_risco:
        tabela = tabela[tabela["risco"].isin(filtro_risco)]
    if busca:
        tabela = tabela[tabela["cidade"].str.contains(busca, case=False, na=False)]

    tabela["risco_ordem"] = tabela["risco"].map(
        {r: i for i, r in enumerate(ORDEM_RISCO)}
    )
    tabela = tabela.sort_values("risco_ordem").drop(columns="risco_ordem")

    st.markdown("<hr style='margin:0.75rem 0 1rem;border:none;border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)

    total = len(tabela)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Cidades exibidas", total)
    with c2:
        if not tabela.empty:
            st.metric("Maior chuva registrada", f"{tabela['chuva'].max():.1f} mm")
    with c3:
        if not tabela.empty:
            st.metric("Maior nível de rio", f"{tabela['nivel_rio'].max():.0f}%")

    st.markdown("<div style='margin-top:1rem;'>", unsafe_allow_html=True)

    if tabela.empty:
        st.info("Nenhum resultado para os filtros aplicados.")
        return

    tabela_exib = tabela[["cidade", "chuva", "nivel_rio", "risco"]].copy()
    tabela_exib.columns = ["Cidade", "Chuva (mm)", "Nível do Rio (%)", "Risco"]

    icones = {"BAIXO": "🟢 BAIXO", "MÉDIO": "🟡 MÉDIO", "ALTO": "🟠 ALTO", "CRÍTICO": "🔴 CRÍTICO"}
    tabela_exib["Risco"] = tabela_exib["Risco"].map(icones)

    st.dataframe(
        tabela_exib,
        use_container_width=True,
        hide_index=True,
        height=min(50 + 35 * len(tabela_exib), 520),
        column_config={
            "Chuva (mm)": st.column_config.NumberColumn(format="%.1f mm"),
            "Nível do Rio (%)": st.column_config.ProgressColumn(
                min_value=0,
                max_value=100,
                format="%.0f%%",
            ),
        },
    )
    st.markdown("</div>", unsafe_allow_html=True)
