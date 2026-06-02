import plotly.express as px


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