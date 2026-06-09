import pandas as pd
import plotly.express as px

def grafico_previsao(previsoes):

    df = pd.DataFrame(
        previsoes
    )

    fig = px.line(
        df,
        x="hora",
        y="chuva",
        markers=True,
        title="Previsão para as Próximas 24 Horas"
    )

    return fig

def grafico_distribuicao_risco(df):

    distribuicao = (
        df["risco"]
        .value_counts()
        .reset_index()
    )

    distribuicao.columns = [
        "risco",
        "quantidade"
    ]

    fig = px.bar(
        distribuicao,
        x="risco",
        y="quantidade",
        title="Distribuição dos Níveis de Risco",
        text="quantidade",
        color="risco"
    )

    return fig

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
