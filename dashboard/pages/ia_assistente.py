import streamlit as st

from dashboard.components.chatbot import (
    render_chat
)


def render():

    st.title("🤖 IA Assistente")

    st.write(
        """
        Assistente virtual para
        análise dos dados da missão.
        """
    )

    render_chat()