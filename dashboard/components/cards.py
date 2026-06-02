import streamlit as st
from src.utils.constantes import COR_BAIXO, COR_MEDIO, COR_ALTO, COR_CRITICO
from src.utils.constantes import BG_BAIXO, BG_MEDIO, BG_ALTO, BG_CRITICO


def _cor_risco(risco: str):
    mapa_cor = {
        "BAIXO":   (COR_BAIXO,   BG_BAIXO),
        "MÉDIO":   (COR_MEDIO,   BG_MEDIO),
        "ALTO":    (COR_ALTO,    BG_ALTO),
        "CRÍTICO": (COR_CRITICO, BG_CRITICO),
    }
    return mapa_cor.get(risco, ("#334155", "#f1f5f9"))


def card_metrica(titulo: str, valor, delta: str = "", icone: str = ""):
    prefixo = f"{icone} " if icone else ""
    st.metric(label=f"{prefixo}{titulo}", value=valor, delta=delta or None)


def card_alerta(cidade: str, risco: str, chuva: float, nivel_rio: float):
    cor, bg = _cor_risco(risco)
    icones = {
        "BAIXO":   "🟢",
        "MÉDIO":   "🟡",
        "ALTO":    "🟠",
        "CRÍTICO": "🔴",
    }
    icone = icones.get(risco, "⚪")
    st.markdown(f"""
    <div style="
        background:{bg};
        border-left: 5px solid {cor};
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    ">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.5rem;">
            <div style="font-size:1.05rem; font-weight:700; color:#1e293b;">
                {icone} {cidade}
            </div>
            <div style="
                background:{cor};
                color:#fff;
                font-size:0.7rem;
                font-weight:700;
                padding:0.2rem 0.65rem;
                border-radius:20px;
                letter-spacing:0.06em;
                text-transform:uppercase;
            ">{risco}</div>
        </div>
        <div style="display:flex; gap:2rem; margin-top:0.25rem;">
            <div>
                <div style="font-size:0.68rem; color:#64748b; text-transform:uppercase; letter-spacing:0.08em;">Chuva</div>
                <div style="font-size:1rem; font-weight:600; color:{cor};">{chuva} mm</div>
            </div>
            <div>
                <div style="font-size:0.68rem; color:#64748b; text-transform:uppercase; letter-spacing:0.08em;">Nível do Rio</div>
                <div style="font-size:1rem; font-weight:600; color:{cor};">{nivel_rio}%</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
