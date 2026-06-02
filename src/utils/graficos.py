import plotly.express as px
import pandas as pd
import plotly.express as px

def grafico_historico():

    df = pd.read_csv(
        "data/historico_chuvas.csv"
    )

    fig = px.line(
        df,
        x="dia",
        y="chuva",
        color="cidade",
        markers=True,
        title="Histórico de Chuvas"
    )

    return fig

def grafico_chuva(df):

    fig = px.bar(
        df,
        x="cidade",
        y="chuva",
        title="Volume de Chuva por Cidade",
        text="chuva"
    )

    return fig


def grafico_rio(df):

    fig = px.bar(
        df,
        x="cidade",
        y="nivel_rio",
        title="Nível dos Rios (%)",
        text="nivel_rio"
    )

    return fig