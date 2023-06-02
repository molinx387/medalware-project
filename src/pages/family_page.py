import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from definition.family_definitions import family_dict

class family_malware(HydraHeadApp):
    def run(self):
        data = pd.read_csv("src/data/malwares.csv")

        title_general = st.container()
        with title_general:
            col1, col2 = st.columns([3, 7])
            col1.title("👾ANÁLISIS DE TIPOS DE familia")
            col1.subheader(
                "📍En este apartado se encuentra informacion individual sobre cada tipo de familia"
            )
            options = data["Familia"].unique()
            familia_selected = col1.selectbox("👇Selecciona tipo de familia👇", options)

            # num_familia = len(options)

            # Obtener la definición y el tipo de la familia de familia seleccionada
            selected_data = data[data["Familia"] == familia_selected]
            selected_data["Fecha"] = pd.to_datetime(selected_data["Fecha"])

            # Contar la cantidad de filas para cada día
            data_grouped_extension = (
                selected_data.groupby(selected_data["Fecha"].dt.date)
                .size()
                .reset_index(name="cantidad")
            )

        # Crear el gráfico de área con Plotly Express
        fig1 = px.histogram(data_grouped_extension, x="Fecha", y="cantidad", nbins=50)

        # Personalizar el diseño del gráfico de área
        fig1.update_layout(
            title=f"Registros del familia {familia_selected}",
            title_x=0.1,
            xaxis_title="Fecha",
            yaxis_title=" Numero de Ocurrencias",
        )

        histograma_familia = col2.container()
        with histograma_familia:
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.plotly_chart(
                fig1,
                config={"displaylogo": False},
                use_container_width=True,
                width=800,
                height=400,
            )
        st.divider()

        definicion = next(
            (
                item["Definicion"]
                for item in family_dict
                if item["Familia"] == familia_selected
            ),
            None,
        )
        


        title_familia = st.container()
        with title_familia:
            # colt1, colt2, colt3 = st.columns([7,5,7])
            col1, col2, col3 = st.columns([2.5, 5, 2.5])
            col4, col5, col6 = st.columns([1, 10, 1])
            col2.markdown(
                f"""
                <div style="text-align: center">
                <h1>☣️{familia_selected}☣️
                <h3>📖
                """,
                unsafe_allow_html=True,
            )
            
            if definicion:
                col2.markdown(
                    f"""
                <div style="text-align: center">
                <h4>{definicion}
                """,
                    unsafe_allow_html=True,
                )
            
            col2.markdown(
                f"""
                <div style="text-align: center">
                <h2> 📑 Analisis del familia {familia_selected}📑
                """,
                unsafe_allow_html=True,
            )

        tag_selector = st.container()
        with tag_selector:
            tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
                [
                    "       📈 Registros",
                    "     🪬Familia",
                    "        🖥Sistema Operativo",
                    "       💾Tipo de Archivo",
                    "       📦Peso",
                    "      📬Metodo de Entrega",
                    "       🌎Origen",
                ]
            )

        total_datos = data["Familia"].value_counts().sum()
        porcentajes = selected_data["Familia"].value_counts() / total_datos * 100

        definicion_familia = st.container()
        with definicion_familia:
            tab1.markdown(
                f"""
                    <div style="text-align: justify">
                    <h4>🔰Medalware a recopliado datos de {selected_data.shape[0]}
                    archivos con el familia {familia_selected} que corresponden al 
                    {porcentajes.iloc[0].round(2)} % de los familias globales analizados
                    por la aplicacion 
                """,
                unsafe_allow_html=True,
            )
            tab4.markdown(
                f"""
                    <div style="text-align: justify">
                    <h4> 🔰 {familia_selected.title()} es un familia que se encuentra mayormente oculto 
                    archivos de extension .{selected_data["Extension"].value_counts().idxmax()}
                    """,
                unsafe_allow_html=True,
            )
            tab5.markdown(
                f"""
                    <div style="text-align: justify">
                    <h4> 🔰 El peso promedio de un archivo {familia_selected.title()} 
                    es de {selected_data["Peso"].mean().round(2)} KB
                    """,
                unsafe_allow_html=True,
            )
            tab6.markdown(
                f"""
                    <div style="text-align: justify">
                    <h4> 🔰 Este tipo de familia infecta llega a los sistemas a traves de
                    {selected_data["Metodo de Entrega"].value_counts().idxmax()}
                    """,
                unsafe_allow_html=True,
            )
            tab7.markdown(
                f"""
                    <div style="text-align: justify">
                    <h4> 🔰 Los datos recopilados de este familia indican que a afectado mayormente al pais 
                    {selected_data["Origen"].value_counts().idxmax()} (ISO 3166-1, alpha-3)
                    """,
                unsafe_allow_html=True,
            )

        data_grouped_mapa = selected_data["Origen"].value_counts()

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
            color_continuous_scale="Viridis",
            labels={"cantidad": "Cantidad"},
            title="Distribución de Origen",
            projection="natural earth",
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

        mapa_familias = tab7.container()
        with mapa_familias:
            col1, col2, col3 = st.columns([3, 7, 3])
            col2.subheader("📌ESPECTRO GLOBAL DE DATOS DE MEDALWARE📌")
            col2.plotly_chart(
                fig5, config={"displaylogo": False}, use_container_width=True
            )

        tabla_familias = tab1.container()
        with tabla_familias:
            st.subheader(f" Registro de datos correspondientes a {familia_selected}")
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.write(
                selected_data[
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

        # Obtener la familia del familia seleccionado
        familia_seleccionada = selected_data["Familia"].iloc[0]
        # Filtrar los datos para incluir solo los familias de la misma familia
        familias_misma_familia = data[data["Familia"] == familia_seleccionada]
        # Agrupar los familias por nombre y contar la cantidad de ocurrencias de cada uno
        datos_agrupados = familias_misma_familia["Familia"].value_counts().reset_index()
        datos_agrupados.columns = ["Familia", "Cantidad"]
        # Calcular la cantidad total de familias de la misma familia
        total_familias_familia = datos_agrupados["Cantidad"].sum()
        # Calcular el porcentaje del familia seleccionado en comparación con otros de la misma familia
        porcentaje_seleccionado = (
            selected_data.shape[0] / total_familias_familia
        ) * 100

        # Mostrar el porcentaje en Streamlit
        tab2.markdown(
            f"""
                <div style="text-align: justify">
                <h4>Este tipo de familia 
                abarca un: {porcentaje_seleccionado:.2f}%
                de los registros de toda la  familia de """,
            unsafe_allow_html=True,
        )
        # Crear la gráfica de dispersión
        fig5 = px.bar(
            datos_agrupados,
            x="Familia",
            y="Cantidad",
            title=f"Gráfica de los familia pertencientes a la familia ",
        )
        # Personalizar el diseño de la gráfica
        fig5.update_layout(xaxis_title="Familia", yaxis_title="Cantidad", title_x=0.25)

        # Mostrar la gráfica en Streamlit
        familias_familias = st.container()
        with familias_familias:
            tab2.plotly_chart(
                fig5,
                config={"displayModeBar": False},
                use_container_width=True,
                width=800,
                height=400,
            )

