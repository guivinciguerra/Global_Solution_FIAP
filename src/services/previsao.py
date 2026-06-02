import random


def gerar_previsao(chuva_atual):

    previsoes = []

    valor = chuva_atual

    for hora in [6, 12, 18, 24]:

        valor += random.randint(
            -5,
            10
        )

        if valor < 0:
            valor = 0

        previsoes.append(
            {
                "hora": hora,
                "chuva": valor
            }
        )

    return previsoes