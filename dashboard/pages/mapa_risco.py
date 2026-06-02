import streamlit as st

from dashboard.components.mapa import exibir_mapa


def render():

    st.title("🗺️ Mapa de Risco")

    st.write(
        """
        Monitoramento geográfico
        das regiões analisadas.
        """
    )

    exibir_mapa()