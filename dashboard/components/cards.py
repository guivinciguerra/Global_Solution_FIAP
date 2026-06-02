import streamlit as st


def card_metrica(titulo, valor):

    st.metric(
        label=titulo,
        value=valor
    )