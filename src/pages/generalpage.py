import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp

class general_malware(HydraHeadApp):
    def run(self):
        st.title("PAGINA GENERAL")
        df = pd.read_csv("src/data/malwares.csv")
        mascabron = df["Familia"].value_counts().idxmax()
        st.header(f"Malware mas concurrente de hoy, [{mascabron}](https://bazaar.abuse.ch/)")

        # Leer el archivo CSV
        data = pd.read_csv("src/data/malwares.csv")

        # Convertir la columna de fecha en formato datetime
        data["Dia"] = pd.to_datetime(data["Dia"])

        # Agrupar por día y contar la cantidad de filas
        data_grouped = data.groupby(data["Dia"].dt.date).size().reset_index(name="cantidad")

        # Crear el histograma con plotly.graph_objects
        # fig = go.Figure(data=[go.Bar(x=data_grouped['Dia'], y=data_grouped['cantidad'])])
        fig = go.Figure([go.Scatter(x=data_grouped["Dia"], y=data_grouped["cantidad"])])

        # Personalizar el diseño del histograma
        fig.update_layout(
            title="Cantidad de Malware por Día",
            xaxis_title="Fecha",
            yaxis_title="Cantidad de Malware",
        )

        # Mostrar el histograma en Streamlit
        st.plotly_chart(fig)


        # Leer el archivo CSV
        data = pd.read_csv("src/data/malwares.csv")

        # Contar la cantidad de filas para cada método de entrega
        data_grouped_metodo = data["Metodo de Entrega"].value_counts()

        # Crear el gráfico de torta para método de entrega con plotly.graph_objects
        fig1 = go.Figure(
            data=[go.Pie(labels=data_grouped_metodo.index, values=data_grouped_metodo.values)]
        )

        # Personalizar el diseño del gráfico de torta para método de entrega
        fig1.update_layout(
            title="Método de Entrega",
            width=300,
            height=300,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada extensión
        data_grouped_extension = data["Extension"].value_counts()

        # Crear el gráfico de torta para extensión con plotly.graph_objects
        fig2 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_extension.index, values=data_grouped_extension.values
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para extensión
        fig2.update_layout(
            title="Extensión", width=300, height=300, margin=dict(l=10, r=10, t=30, b=10)
        )

        # Crear la primera columna con los dos gráficos de torta
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)

        # Contar la cantidad de filas para cada método de familia
        data_grouped_metodo = data["Familia"].value_counts()

        # Crear el gráfico de torta para método de entrega con plotly.graph_objects
        fig3 = go.Figure(
            data=[go.Pie(labels=data_grouped_metodo.index, values=data_grouped_metodo.values)]
        )

        # Personalizar el diseño del gráfico de torta para método de entrega
        fig3.update_layout(
            title="Familia de Malware",
            width=300,
            height=300,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada origen
        data_grouped_extension = data["Origen"].value_counts()

        # Crear el gráfico de torta para extensión con plotly.graph_objects
        fig4 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_extension.index, values=data_grouped_extension.values
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para origen
        fig4.update_layout(
            title="Origen", width=300, height=300, margin=dict(l=10, r=10, t=30, b=10)
        )

        # Crear la segunda columna con los dos gráficos de torta
        with col2:
            st.plotly_chart(fig3)
            st.plotly_chart(fig4)


        # Leer el archivo CSV
        data = pd.read_csv("src/data/malwares.csv")

        # Mostrar el cuadro de datos en Streamlit con un subtítulo
        st.subheader("Tabla de Malwares")
        st.write(
            data[
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
