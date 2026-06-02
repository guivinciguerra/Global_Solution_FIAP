def classificar_risco(chuva, nivel_rio):

    if chuva >= 80 or nivel_rio >= 90:
        return "CRÍTICO"

    elif chuva >= 60 or nivel_rio >= 75:
        return "ALTO"

    elif chuva >= 30 or nivel_rio >= 50:
        return "MÉDIO"

    return "BAIXO"