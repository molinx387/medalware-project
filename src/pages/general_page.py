import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from streamlit_extras.mandatory_date_range import date_range_picker

class general_malware(HydraHeadApp):
    def run(self):
        data = pd.read_csv("src/data/malwares.csv")
        titel_general = st.container()
        with titel_general:
            col1,col2 = st.columns([4,6])
            col1.title("🔖  ANÁLISIS GENERALES ")
            col1.markdown(
            """
            <div style="text-align: justify">
            En este apartado se encuentran análisis de datos generales\n sobre todos los registros de datos de Medalware.
            </div>
            """,
            unsafe_allow_html=True)














            # mascabron = data["Familia"].value_counts().idxmax()
            # st.header(
                # f"Malware mas concurrente de hoy, [{mascabron}](https://bazaar.abuse.ch/)"
            # )
        
        # Convertir la columna de fecha en formato datetime
        data["Dia"] = pd.to_datetime(data["Dia"])

        date_range = date_range_picker("Select a date range")
        start_date = pd.to_datetime(date_range[0]).date()
        end_date = pd.to_datetime(date_range[1]).date()

        filtered_data = data[(data["Dia"].dt.date >= start_date) & (data["Dia"].dt.date <= end_date)]

        data_grouped = (
            filtered_data.groupby(filtered_data["Dia"].dt.date).size().reset_index(name="cantidad")
        )

        # Crear el gráfico de área con Plotly Express
        fig = px.area(data_grouped, x="Dia", y="cantidad")

        # Personalizar el diseño del gráfico de área
        fig.update_layout(
            title="Cantidad de Malware por Día",
            xaxis_title="Fecha",
            yaxis_title="Cantidad de Malware",
            )

        # Mostrar el gráfico en Streamlit
        histograma_malwares = st.container()
        with histograma_malwares:
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.plotly_chart(fig, config = {'displaylogo': False}, use_container_width=True, width=800, height=400)

        # Personalizar Colores de las gráficas de torta
        colors = px.colors.qualitative.G10

        # Contar la cantidad de filas para cada método de entrega
        data_grouped_metodo = filtered_data["Metodo de Entrega"].value_counts().head(6)

        # Crear el gráfico de torta para método de entrega con plotly.graph_objects
        fig1 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_metodo.index, values=data_grouped_metodo.values
                )
            ]
        )


        # Personalizar el diseño del gráfico de torta para método de entrega
        fig1.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )

        fig1.update_layout(
            title="Método de Entrega",
            width=400,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada extensión
        data_grouped_extension = filtered_data["Extension"].value_counts().head(6)

        # Crear el gráfico de torta para extensión con plotly.graph_objects
        fig2 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_extension.index,
                    values=data_grouped_extension.values,
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para extensión
        fig2.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )
        fig2.update_layout(
            title="Extensión",
            width=400,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Crear la primera columna con los dos gráficos de torta
        col1, col2 = st.columns([3, 2])
        with col1:
            st.plotly_chart(fig1, config = {'displayModeBar': False})
            st.plotly_chart(fig2, config = {'displayModeBar': False})

        # Contar la cantidad de filas para cada método de familia
        data_grouped_metodo = filtered_data["Familia"].value_counts().head(6)

        # Crear el gráfico de torta para método de entrega con plotly.graph_objects
        fig3 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_metodo.index, values=data_grouped_metodo.values
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para método de entrega
        fig3.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )
        fig3.update_layout(
            title="Familia de Malware",
            width=400,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada origen
        data_grouped_extension_origen = filtered_data["Origen"].value_counts()

        # Tomar solo los primeros 6 datos
        data_grouped_extension_origen  = data_grouped_extension_origen .head(6)

        # Crear el gráfico de torta para extensión con plotly.graph_objects
        fig4 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_extension_origen .index,
                    values=data_grouped_extension_origen .values,
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para origen
        fig4.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )
        fig4.update_layout(
            title="Origen", width=400, height=400, margin=dict(l=10, r=10, t=30, b=10)
        )

        # Crear la segunda columna con los dos gráficos de torta
        with col2:
            st.plotly_chart(fig3, config = {'displayModeBar': False})
            st.plotly_chart(fig4, config = {'displayModeBar': False})

        tabla_malwares = st.container()
        with tabla_malwares:
            st.subheader("Tabla de Malwares")
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.write(
            filtered_data[
                    [
                        "SHA256",
                        "Familia",
                        "Extension",
                        "Peso (MB)",
                        "Metodo de Entrega",
                        "Origen",
                        "Dia",
                        "Hora",
                    ]
                ]
            )

        # Contar la cantidad de filas para cada origen del mapa
        data_grouped_extension= filtered_data["Origen"].value_counts()

        # Crear el DataFrame con los datos de cantidad por origen
        data = pd.DataFrame({'iso_alpha': data_grouped_extension.index,
                     'cantidad': data_grouped_extension.values})

        # Crear el gráfico de mapa coroplético interactivo
        fig5 = px.choropleth(data_frame=data, locations='iso_alpha', locationmode='ISO-3',
                            color='cantidad', color_continuous_scale='Viridis',
                            labels={'cantidad': 'Cantidad'},
                            title='Distribución de Origen',
                            projection='orthographic')

        fig5.update_geos(showland=True, showocean=True, showcountries=True, showframe=True,
                landcolor='white', oceancolor='white', bgcolor='rgba(0,0,0,0)')
        
        fig5.update_layout(
        width=800,
        height=600
        )

        # Mostrar el gráfico en Streamlit
        mapa_malwares = st.container()
        with mapa_malwares:
            st.subheader("Mapa de Malwares")
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.plotly_chart(fig5, config = {'displaylogo': False}, use_container_width=True)
