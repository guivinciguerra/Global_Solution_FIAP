from src.utils.loaders import (
    carregar_simulacao
)

from src.services.analisador import (
    analisar_cidades
)


def responder(pergunta):

    df = carregar_simulacao()

    df = analisar_cidades(df)

    pergunta = pergunta.lower()

    if "maior risco" in pergunta:

        cidade = df.sort_values(
            "nivel_rio",
            ascending=False
        ).iloc[0]

        return (
            f"{cidade['cidade']} "
            f"possui o maior risco "
            f"atualmente."
        )

    if "crítico" in pergunta:

        cidades = df[
            df["risco"] == "CRÍTICO"
        ]

        return (
            f"Existem {len(cidades)} "
            f"cidades em risco crítico."
        )

    return (
        "Tente perguntar sobre "
        "risco ou enchentes."
    )