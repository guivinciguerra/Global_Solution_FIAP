import pandas as pd
import folium

from streamlit_folium import st_folium

from src.utils.loaders import carregar_simulacao
from src.services.analisador import analisar_cidades


def cor_risco(risco):

    cores = {
        "BAIXO": "green",
        "MÉDIO": "orange",
        "ALTO": "red",
        "CRÍTICO": "darkred"
    }

    return cores.get(
        risco,
        "blue"
    )


def criar_mapa():

    simulacao = carregar_simulacao()

    simulacao = analisar_cidades(
        simulacao
    )

    coordenadas = pd.read_csv(
        "data/coordenadas.csv"
    )

    df = simulacao.merge(
        coordenadas,
        on="cidade"
    )

    mapa = folium.Map(
        location=[-23.55, -46.63],
        zoom_start=7
    )

    for _, row in df.iterrows():

        popup = f"""
        <b>{row['cidade']}</b><br>
        Chuva: {row['chuva']} mm<br>
        Rio: {row['nivel_rio']}%<br>
        Risco: {row['risco']}
        """

        folium.Marker(
            [row['latitude'], row['longitude']],
            popup=popup,
            icon=folium.Icon(
                color=cor_risco(
                    row['risco']
                )
            )
        ).add_to(mapa)

    return mapa


def exibir_mapa():

    st_folium(
        criar_mapa(),
        width=1200,
        height=600
    )