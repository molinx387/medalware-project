import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp


class delivery_malware(HydraHeadApp):
    def run(self):
        data = pd.read_csv("src/data/malwares.csv")
        title = st.container()
        with title:
            col1, col2 = st.columns([5, 6])
            col1.title("ANÁLISIS DE MÉTODOS DE ENTREGA DE MALWARE")
            col1.subheader(
                "📌En este apartado se encuentra información sobre las formas en la que el malware llega a los sistemas"
            )
            options = data["Familia"].unique()
            options = data["Metodo de Entrega"].unique()
            entraga_selected = col1.selectbox("👇Selecciona un Método de Entrega👇", options)
            selected_data_metodo = data[data["Metodo de Entrega"] == entraga_selected]
            colt1, colt2, colt3 = st.columns([6, 6, 6])
            col1.title(f"📥{entraga_selected.title()}📥")
            st.divider()
            # col2.image("src/media/method.png")

        # Personalizar Colores de las gráficas de torta
        colors = px.colors.qualitative.G10
        # Contar la cantidad de filas para cada Sistema operativo
        data_metodo = data["Metodo de Entrega"].value_counts()
        # Crear el gráfico de torta para Sistema operativo con plotly.graph_objects
        fig1 = go.Figure(
            data=[
                go.Pie(
                    labels=data_metodo.index,
                    values=data_metodo.values,
                    pull=[0.1, 0.1, 0.1, 0.1, 0.1],
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para Sistema operativo
        fig1.update_traces(
            textposition="outside",
            textinfo="percent+label",
            textfont_size=14,
            marker=dict(colors=colors, line=dict(color=colors, width=1)),
        )
        fig1.update_layout(
            width=600,
            height=500,
            margin=dict(l=80, r=0, t=0, b=130),
        )
        fig1.update(layout_showlegend=False)

        grafica_pie = col2.container()
        with grafica_pie:
            st.plotly_chart(fig1, config={"displaylogo": False})

        tabla_descarga_wed = st.container()
        with tabla_descarga_wed:
            col1, col2, col3 = st.columns([0.1, 5, 0.1])
            col2.subheader(
                f"📋⬇️Registro de datos de malwares que fueron registrados mediante {entraga_selected}📋⬇️"
            )
            col2.write(
                selected_data_metodo[
                    [
                        "Fecha",
                        "SHA256",
                        "Malware",
                        "Familia",
                        "SO",
                        "Metodo de Entrega",
                        "Extension",
                        "Peso",
                        "Origen",
                    ]
                ]
            )

        data_malware = selected_data_metodo["Malware"].value_counts()
        fig2 = px.bar(data_malware, x=data_malware.index, y=data_malware.values)
        fig2.update_layout(
            title=f" ",
            title_x=0.4,
            xaxis_title="Malware",
            yaxis_title="Cantidad",
        )
        
        st.subheader(f"🔻Gráfico de malwares registrados empleando la  {entraga_selected} como método de entrega🔻")
        # Mostrar la gráfica en Streamlit
        familias_familias = st.container()
        with familias_familias:
            st.plotly_chart(
                fig2,
                config={"displayModeBar": False},
                use_container_width=True,
                width=800,
                height=400,
            )
        data_malware = selected_data_metodo["Familia"].value_counts()
        fig = px.bar(data_malware, x=data_malware.index, y=data_malware.values)
        fig.update_layout(
            title=f" ",
            title_x=0.2,
            xaxis_title="Malware",
            yaxis_title="Cantidad",
        )
        st.subheader(f"🔻Familias de malware que emplearon {entraga_selected} para llegar a los sistemas-usuarios🔻")

        # Mostrar la gráfica en Streamlit
        familias_familias = st.container()
        with familias_familias:
            st.plotly_chart(
                fig,
                config={"displayModeBar": False},
                use_container_width=True,
                width=800,
                height=400,
            )

        data_grouped_mapa = selected_data_metodo["Origen"].value_counts()

        # Crear el DataFrame con los datos de cantidad por origen
        data_map = pd.DataFrame(
            {"iso_alpha": data_grouped_mapa.index, "cantidad": data_grouped_mapa.values}
        )

        # Crear el gráfico de mapa coroplético interactivo
        fig5 = px.choropleth(
            data_frame=data_map,
            locations="iso_alpha",
            locationmode="ISO-3",
            color="cantidad",
            title=f" ",
            color_continuous_scale="portland",
            labels={"cantidad": "Cantidad"},
            projection="equirectangular",
        )

        fig5.update_geos(
            showland=True,
            showocean=True,
            showcountries=True,
            showframe=True,
            landcolor="white",
            oceancolor="white",
            bgcolor="rgba(0,0,0,0)",
        )

        fig5.update_layout(width=550, height=500)
        st.subheader(f"🔻Paises en donde la {entraga_selected} es el método de entrega de malware más común🔻")
        mapa_malwares = st.container()
        with mapa_malwares:
            st.plotly_chart(
                fig5, config={"displaylogo": False}, use_container_width=True
            )
