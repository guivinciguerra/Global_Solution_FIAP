def responder(pergunta):

    pergunta = pergunta.lower()

    if "risco" in pergunta:

        return (
            "A região monitorada "
            "apresenta risco elevado "
            "de enchentes."
        )

    elif "chuva" in pergunta:

        return (
            "O volume de chuva "
            "está acima da média."
        )

    elif "cidade" in pergunta:

        return (
            "São Paulo possui "
            "o maior nível de risco."
        )

    return (
        "Não encontrei uma resposta "
        "para essa pergunta."
    )