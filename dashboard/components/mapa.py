import folium
from streamlit_folium import st_folium


def criar_mapa():

    mapa = folium.Map(
        location=[-23.55, -46.63],
        zoom_start=7
    )

    cidades = [
        {
            "nome": "São Paulo",
            "lat": -23.55,
            "lon": -46.63,
            "risco": "CRÍTICO"
        },
        {
            "nome": "Campinas",
            "lat": -22.90,
            "lon": -47.06,
            "risco": "MÉDIO"
        },
        {
            "nome": "Santos",
            "lat": -23.96,
            "lon": -46.33,
            "risco": "ALTO"
        }
    ]

    for cidade in cidades:

        cor = "green"

        if cidade["risco"] == "MÉDIO":
            cor = "orange"

        elif cidade["risco"] == "ALTO":
            cor = "red"

        elif cidade["risco"] == "CRÍTICO":
            cor = "darkred"

        folium.Marker(
            [cidade["lat"], cidade["lon"]],
            popup=f"{cidade['nome']} - {cidade['risco']}",
            icon=folium.Icon(color=cor)
        ).add_to(mapa)

    return mapa


def exibir_mapa():

    st_folium(
        criar_mapa(),
        width=1200,
        height=600
    )