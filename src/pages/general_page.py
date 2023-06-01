import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from streamlit_extras.mandatory_date_range import date_range_picker
import pycountry


def percentages(data_grouped):
    total_datos = data_grouped.sum()
    percentage = data_grouped / total_datos * 100
    return percentage[0].round(2)


class general_malware(HydraHeadApp):
    def run(self):
        data = pd.read_csv("src/data/malwares.csv")
        titel_general = st.container()
        with titel_general:
            col1, col2 = st.columns([3, 7])
            col1.title("🔖ANÁLISIS GENERALES ")
            col1.subheader(
                "En este apartado se encuentran análisis de los datos recopilados por Medalware"
            )
            # col2.markdown(
            # """
            # <div style="text-align: justify">
            # En este apartado se encuentran análisis de los datos recopilados por Medalware
            # </div>
            # """,
            # unsafe_allow_html=True)
            # mascabron = data["Familia"].value_counts().idxmax()
            # st.header(
            # f"Malware mas concurrente de hoy, [{mascabron}](https://bazaar.abuse.ch/)"
            # )

        # Convertir la columna de fecha en formato datetime
        data["Fecha"] = pd.to_datetime(data["Fecha"])
        with col1:
            date_range = date_range_picker(
                "_SELECCIONA UN RANGO DE TIEMPO PARA VER LOS REGISTROS_"
            )
            start_date = pd.to_datetime(date_range[0]).date()
            end_date = pd.to_datetime(date_range[1]).date()

            filtered_data = data[
                (data["Fecha"].dt.date >= start_date)
                & (data["Fecha"].dt.date <= end_date)
            ]

            data_grouped = (
                filtered_data.groupby(filtered_data["Fecha"].dt.date)
                .size()
                .reset_index(name="cantidad")
            )
        st.divider()
        # Crear el gráfico de área con Plotly Express
        fig = px.area(data_grouped, x="Fecha", y="cantidad")

        # Personalizar el diseño del gráfico de área
        fig.update_layout(
            title=f"Registro de Malware Analizados desde {start_date} hasta {end_date}",
            title_x=0.1,
            xaxis_title="Fecha",
            yaxis_title="Numero de Malwares",
        )

        # Mostrar el gráfico en Streamlit
        histograma_malwares = col2.container()
        with histograma_malwares:
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.plotly_chart(
                fig,
                config={"displaylogo": False},
                use_container_width=True,
                width=800,
                height=400,
            )

        title_analisis = st.container()
        with title_analisis:
            col1, col2, col3 = st.columns([1, 8, 1])
            col4, col5, col6 = st.columns([2.2, 8, 2.2])
            col2.title(f"📑 ANÁLISIS GENERAL {start_date} AL {end_date}📑")
            col5.markdown(
                f"""
                <div style="text-align: justify">
                <h4>Medalware ha
                recopilado, limpiado y analizado los datos de alrededor
                de {filtered_data.shape[0]} nuevos malwares,
                con lo que se ha podido extraer la siguiente informacion:

            """,
                unsafe_allow_html=True,
            )
        # Personalizar Colores de las gráficas de torta
        colors = px.colors.qualitative.G10

        # Contar la cantidad de filas para cada método de entrega
        data_grouped_metodo_entrega = (
            filtered_data["Metodo de Entrega"].value_counts().head(6)
        )

        # Crear el gráfico de torta para método de entrega con plotly.graph_objects
        fig1 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_metodo_entrega.index,
                    values=data_grouped_metodo_entrega.values,
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
            title=f"Métodos de entrega más comunes",
            width=500,
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
            title=f"Extensiones usadas por malware",
            width=400,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada método de familia
        data_grouped_malware = filtered_data["Malware"].value_counts().head(6)

        # Crear el gráfico de torta para método de entrega con plotly.graph_objects
        fig3 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_malware.index,
                    values=data_grouped_malware.values,
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
            title=f"Top malwares",
            width=450,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada origen
        data_grouped_origen = filtered_data["Origen"].value_counts().head(6)

        # Crear el gráfico de torta para extensión con plotly.graph_objects
        fig4 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_origen.index,
                    values=data_grouped_origen.values,
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
            title=f"Top mayor registro de malware",
            width=400,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada familia
        data_grouped_familia = filtered_data["Familia"].value_counts().head(6)

        # Crear el gráfico de torta para familia con plotly.graph_objects
        fig6 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_familia.index,
                    values=data_grouped_familia.values,
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para familia
        fig6.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )
        fig6.update_layout(
            title=f"Top Familas de malware",
            width=450,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

         # Contar la cantidad de filas para cada Sistema operativo
        data_grouped_origen = filtered_data["SO"].value_counts().head(6)

        # Crear el gráfico de torta para Sistema operativo con plotly.graph_objects
        fig7 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_origen.index,
                    values=data_grouped_origen.values,
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para Sistema operativo
        fig7.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )
        fig7.update_layout(
            title=f"Top Sistema operativo",
            width=500,
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        def percentaje(data_grouped):
            total_datos = data_grouped.sum()
            porcentajes = data_grouped / total_datos * 100
            return porcentajes[0].round(2)

        def obtener_nombre_pais(codigo_iso3):
            return pycountry.countries.get(alpha_3=codigo_iso3).name

        # Crear la columna con los dos gráficos de torta
        col1, col2 = st.columns([6, 6])
        with col1:
            pie6_1, pie6_2, pie6_3 = st.columns([2, 7, 3])
            pie6_2.plotly_chart(fig6, config={"displaylogo": False})
            with st.expander("🪤"):
                st.markdown(
                    f"""
                <h4> Hasta la fecha, los {filtered_data["Familia"].value_counts().idxmax()} han sido 
                la familia de malware más predominante, representando aproximadamente el 
                {percentages(data_grouped_familia)}% del total de amenazas.
                """,
                    unsafe_allow_html=True,
                )
                st.divider()
            pie1_1, pie1_2, pie1_3 = st.columns([2, 7, 3])
            pie1_2.plotly_chart(fig1, config={"displaylogo": False})
            with st.expander("🪤"):
                st.markdown(
                    f"""
                <h4> 🪤 El metodo de entrega más utilizado por los ciberdelincuentes es la
                {filtered_data["Metodo de Entrega"].value_counts().idxmax()}, con un 
                {percentages(data_grouped_metodo_entrega)}% sobre otros metodos convencionales.
                """,
                    unsafe_allow_html=True,
                )
                st.divider()
            pie3_1, pie3_2, pie3_3 = st.columns([2, 7, 3])
            pie3_2.plotly_chart(fig3, config={"displaylogo": False})
            with st.expander("👾"):
                st.markdown(
                    f"""
                <h4> 👾 El malware más concurrente hasta la fecha es
                {filtered_data["Malware"].value_counts().idxmax()},
                que abarca un {percentages(data_grouped_malware)}% de todo el conjunto de malwares
                """,
                    unsafe_allow_html=True,
                )
                st.divider()

        with col2:
            pie7_1, pie7_2, pie7_3 = st.columns([2, 7, 3])
            pie7_2.plotly_chart(fig7, config={"displaylogo": False})
            with st.expander("⚙️"):
                st.markdown(
                    f"""
                <h4>⚙️ El tipo de archivo más utilizado por los ciberdelincuentes son aquellos correspondientes 
                a la extension ".{filtered_data["Extension"].value_counts().idxmax()}" que representan un 
                {percentages(data_grouped_extension)}% del conjunto total.
                """,
                    unsafe_allow_html=True,
                )
                st.divider()
            pie2_1, pie2_2, pie2_3 = st.columns([2, 7, 3])
            pie2_2.plotly_chart(fig2, config={"displaylogo": False})
            with st.expander("⚙️"):
                st.markdown(
                    f"""
                <h4>⚙️ El tipo de archivo más utilizado por los ciberdelincuentes son aquellos correspondientes 
                a la extension ".{filtered_data["Extension"].value_counts().idxmax()}" que representan un 
                {percentages(data_grouped_extension)}% del conjunto total.
                """,
                    unsafe_allow_html=True,
                )
                st.divider()

            pie4_1, pie4_2, pie4_3 = st.columns([2, 7, 3])
            pie4_2.plotly_chart(fig4, config={"displaylogo": False})
            with st.expander("🌎"):
                st.markdown(
                    f"""
                <h4>🌎 {obtener_nombre_pais('FRA')} destaca como el país con el mayor registro de malware, 
                representando aproximadamente el {percentages(data_grouped_origen)}% en comparación con otras naciones.
                """,
                    unsafe_allow_html=True,
                )
                st.divider()

        st.divider()
        tabla_malwares = st.container()
        with tabla_malwares:
            st.subheader("REGISTRO DE DATOS ")
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.write(
                filtered_data[
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

        # Contar la cantidad de filas para cada origen del mapa
        data_grouped_mapa = filtered_data["Origen"].value_counts()

        # Crear el DataFrame con los datos de cantidad por origen
        data = pd.DataFrame(
            {"iso_alpha": data_grouped_mapa.index, "cantidad": data_grouped_mapa.values}
        )

        # Crear el gráfico de mapa coroplético interactivo
        fig5 = px.choropleth(
            data_frame=data,
            locations="iso_alpha",
            locationmode="ISO-3",
            color="cantidad",
            color_continuous_scale="Viridis",
            labels={"cantidad": "Cantidad"},
            title="Distribución de Origen",
            projection="orthographic",
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

        fig5.update_layout(width=800, height=600)

        # Mostrar el gráfico en Streamlit
        mapa_malwares = st.container()
        with mapa_malwares:
            col1, col2, col3 = st.columns([3, 7, 3])
            col2.subheader("📌ESPECTRO GLOBAL DE DATOS DE MEDALWARE📌")
            col2.plotly_chart(
                fig5, config={"displaylogo": False}, use_container_width=True
            )
