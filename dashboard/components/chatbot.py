import streamlit as st

from src.services.ia_service import responder


def render_chat():

    pergunta = st.text_input(
        "Faça uma pergunta"
    )

    if st.button("Enviar"):

        resposta = responder(
            pergunta
        )

        st.success(resposta)