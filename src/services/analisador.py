from src.services.classificacao import classificar_risco


def analisar_cidades(df):

    df = df.copy()

    df["risco"] = df.apply(
        lambda row: classificar_risco(
            row["chuva"],
            row["nivel_rio"]
        ),
        axis=1
    )

    return df