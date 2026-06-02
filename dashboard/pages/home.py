import streamlit as st
import pandas as pd
from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades
from src.utils.constantes import ORDEM_RISCO


def _badge_risco(risco: str) -> str:
    cores = {
        "BAIXO":   ("#1D9E75", "#EAF3DE"),
        "MÉDIO":   ("#BA7517", "#FAEEDA"),
        "ALTO":    ("#D85A30", "#FAECE7"),
        "CRÍTICO": ("#A32D2D", "#FCEBEB"),
    }
    icones = {"BAIXO": "🟢", "MÉDIO": "🟡", "ALTO": "🟠", "CRÍTICO": "🔴"}
    cor, bg = cores.get(risco, ("#334155", "#f1f5f9"))
    icone = icones.get(risco, "⚪")
    return (
        f'<span style="background:{bg};color:{cor};border:1px solid {cor}33;'
        f'padding:0.15rem 0.55rem;border-radius:20px;font-size:0.75rem;font-weight:700;">'
        f'{icone} {risco}</span>'
    )


def render():
    st.markdown("## Centro de Operações")
    st.markdown(
        "<p style='color:#64748b;margin-top:-0.5rem;margin-bottom:1.5rem;font-size:0.9rem;'>"
        "Visão geral do monitoramento hidrológico e meteorológico em tempo real."
        "</p>",
        unsafe_allow_html=True,
    )

    df = carregar_simulacao()
    df = analisar_cidades(df)

    total = len(df)
    criticos = len(df[df["risco"] == "CRÍTICO"])
    altos = len(df[df["risco"] == "ALTO"])
    media_chuva = round(df["chuva"].mean(), 1)
    media_rio = round(df["nivel_rio"].mean(), 1)

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.metric("📍 Cidades Monitoradas", total)
    with c2:
        st.metric("🔴 Situações Críticas", criticos, delta=None)
    with c3:
        st.metric("🟠 Alertas Ativos", altos)
    with c4:
        st.metric("🌧 Chuva Média", f"{media_chuva} mm")
    with c5:
        st.metric(" Nível Médio dos Rios", f"{media_rio}%")

    st.markdown("<hr style='margin:1.5rem 0;border:none;border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)

    col_tabela, col_resumo = st.columns([3, 2], gap="large")

    with col_tabela:
        st.markdown("### Indicadores Operacionais")
        tabela = df[["cidade", "chuva", "nivel_rio", "risco"]].copy()
        tabela["risco_ordem"] = tabela["risco"].map(
            {r: i for i, r in enumerate(ORDEM_RISCO)}
        )
        tabela = tabela.sort_values("risco_ordem").drop(columns="risco_ordem")
        tabela.columns = ["Cidade", "Chuva (mm)", "Nível do Rio (%)", "Risco"]

        st.dataframe(
            tabela,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Chuva (mm)": st.column_config.NumberColumn(format="%.1f mm"),
                "Nível do Rio (%)": st.column_config.ProgressColumn(
                    min_value=0,
                    max_value=100,
                    format="%.0f%%",
                ),
            },
        )

    with col_resumo:
        st.markdown("### Resumo Executivo")

        distribuicao = df["risco"].value_counts().reindex(ORDEM_RISCO, fill_value=0)
        for nivel, qtd in distribuicao.items():
            if qtd == 0:
                continue
            cores = {
                "CRÍTICO": "#A32D2D",
                "ALTO":    "#D85A30",
                "MÉDIO":   "#BA7517",
                "BAIXO":   "#1D9E75",
            }
            bgs = {
                "CRÍTICO": "#FCEBEB",
                "ALTO":    "#FAECE7",
                "MÉDIO":   "#FAEEDA",
                "BAIXO":   "#EAF3DE",
            }
            cor = cores.get(nivel, "#334155")
            bg = bgs.get(nivel, "#f1f5f9")
            st.markdown(f"""
            <div style="background:{bg};border-left:4px solid {cor};border-radius:6px;
                        padding:0.6rem 1rem;margin-bottom:0.5rem;display:flex;
                        align-items:center;justify-content:space-between;">
                <span style="font-size:0.85rem;font-weight:600;color:{cor};">{nivel}</span>
                <span style="font-size:1.1rem;font-weight:800;color:{cor};">{qtd}
                    <span style="font-size:0.72rem;font-weight:400;color:#64748b;">cidade{'s' if qtd > 1 else ''}</span>
                </span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='margin-top:1rem;'>", unsafe_allow_html=True)
        if criticos > 0:
            st.error(
                f"**Atenção:** {criticos} região{'ões' if criticos > 1 else ''} "
                f"em situação crítica. Acesse **Alertas** para detalhes.",
                icon="🚨",
            )
        elif altos > 0:
            st.warning(
                f"{altos} região{'ões' if altos > 1 else ''} em nível de alerta. "
                f"Monitoramento recomendado.",
                icon="⚠️",
            )
        else:
            st.success("Todas as regiões operam dentro dos parâmetros normais.", icon="✅")
        st.markdown("</div>", unsafe_allow_html=True)
