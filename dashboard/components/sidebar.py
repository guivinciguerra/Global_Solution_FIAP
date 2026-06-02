import streamlit as st
from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades


def render_sidebar():
    df = carregar_simulacao()
    df = analisar_cidades(df)
    criticos = len(df[df["risco"] == "CRÍTICO"])
    altos = len(df[df["risco"] == "ALTO"])
    total = len(df)

    if criticos > 0:
        status_cor = "#ff4b4b"
        status_txt = "⚠ ATENÇÃO ELEVADA"
    elif altos > 0:
        status_cor = "#D85A30"
        status_txt = "◉ SITUAÇÃO DE ALERTA"
    else:
        status_cor = "#1D9E75"
        status_txt = "● OPERAÇÃO ESTÁVEL"

    st.sidebar.markdown(f"""
    <div style="padding: 1.2rem 0.5rem 0.8rem;">
        <div style="font-size:1.4rem; font-weight:800; letter-spacing:0.03em; color:#ffffff;">
            FloodWatch
        </div>
        <div style="font-size:0.72rem; color:#94a3b8; margin-top:0.2rem; text-transform:uppercase; letter-spacing:0.08em;">
            Plataforma de Monitoramento Hidrológico
        </div>
    </div>
    <div style="background:#1e2d42; border-radius:8px; padding:0.75rem 1rem; margin:0 0.5rem 1rem;">
        <div style="font-size:0.65rem; color:#64748b; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.3rem;">Status do sistema</div>
        <div style="font-size:0.82rem; font-weight:700; color:{status_cor};">{status_txt}</div>
    </div>
    <div style="display:flex; gap:0.5rem; margin:0 0.5rem 1.2rem; justify-content:space-between;">
        <div style="flex:1; background:#1e2d42; border-radius:7px; padding:0.55rem 0.5rem; text-align:center;">
            <div style="font-size:1.1rem; font-weight:800; color:#ffffff;">{total}</div>
            <div style="font-size:0.62rem; color:#64748b; margin-top:0.1rem;">Cidades</div>
        </div>
        <div style="flex:1; background:#1e2d42; border-radius:7px; padding:0.55rem 0.5rem; text-align:center;">
            <div style="font-size:1.1rem; font-weight:800; color:#D85A30;">{altos}</div>
            <div style="font-size:0.62rem; color:#64748b; margin-top:0.1rem;">Alertas</div>
        </div>
        <div style="flex:1; background:#1e2d42; border-radius:7px; padding:0.55rem 0.5rem; text-align:center;">
            <div style="font-size:1.1rem; font-weight:800; color:#ff4b4b;">{criticos}</div>
            <div style="font-size:0.62rem; color:#64748b; margin-top:0.1rem;">Críticos</div>
        </div>
    </div>
    <div style="font-size:0.68rem; color:#64748b; text-transform:uppercase; letter-spacing:0.1em; padding:0 0.5rem 0.5rem;">
        Navegação
    </div>
    """, unsafe_allow_html=True)
