import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from definition.family_definitions import family_dict
from streamlit_extras.add_vertical_space import add_vertical_space


class family_malware(HydraHeadApp):
    def run(self):
        data = pd.read_csv("src/data/malwares.csv")

        title_general = st.container()
        with title_general:
            col1, col2 = st.columns([3, 7])
            col1.title("ANÁLISIS DE DATOS DE FAMILIAS DE MALWARE")
            col1.subheader(
                "📌En este apartado se encuentra informacion relativa a los registros de familias de malware"
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
            col1, col2 = st.columns([6, 5])
            col4, col5, col6 = st.columns([1, 10, 1])
            col1.markdown(
                f"""
                <div style="text-align: left">
                <h1>☣️{familia_selected}☣️
                """,
                unsafe_allow_html=True,
            )

            if definicion:
                col2.markdown(
                    f"""
                <div style="text-align: justify">
                <h4>{definicion}
                """,
                    unsafe_allow_html=True,
                )
            col1.markdown(
                f"""
                <div style="text-align: left">
                <h4> ⬇️📑 Información analizada a partir de los datos de {familia_selected}
                """,
                unsafe_allow_html=True,
            )
        tag_selector = st.container()
        with tag_selector:
            tab1, tab2, tab3, tab4 = st.tabs(
                [
                    "       📈Registros",
                    "       📂Malwares constitutivos",
                    "       📊Caracteristicas",
                    "       🌎Origen",
                ]
            )

        total_datos = data["Familia"].value_counts().sum()
        porcentajes = selected_data["Familia"].value_counts() / total_datos * 100

        registro_familia = st.container()
        with registro_familia:
            tab1.markdown(
                f"""
                    <div style="text-align: center">
                    <h4>🔰Medalware ha recopliado datos de {selected_data.shape[0]}
                    malwares pertenecientes a la familia {familia_selected}🔰
                    <h4>🔸La constitucion numerica de esta familia abarca un {porcentajes.iloc[0].round(2)} % 
                    del total con respecto a las otras familias recopiladas por la aplicacion🔸 
                """,
                unsafe_allow_html=True,
            )

        col1_2, col2_2, col3_2 = tab3.columns([4, 4, 4])
        caracteristicas = tab3.container()
        with caracteristicas:
            col1_2.markdown(
                f"""
                        <div style="text-align: center">
                        <h4>🔴{familia_selected} es una familia de malware que 
                        afecta principalmente a sistemas  {selected_data["SO"].value_counts().idxmax()}
                        """,
                unsafe_allow_html=True,
            )
            col2_2.markdown(
                f"""
                        <div style="text-align: center">
                        <h4>🟠La mayoria de los malwares pertenecientes a la familia
                        {familia_selected.title()} se ejecutan bajo archivos de extension 
                        .{selected_data["Extension"].value_counts().idxmax()}
                        """,
                unsafe_allow_html=True,
            )
            col3_2.markdown(
                f"""
                        <div style="text-align: center">
                        <h4>🟢 Un {familia_selected}
                        se caracteriza por ingresar a los sistemas a traves de
                        {selected_data["Metodo de Entrega"].value_counts().idxmax()}
                        """,
                unsafe_allow_html=True,
            )
        col1_m, col2_m = tab4.columns([7, 3])
        origen_tab4 = st.container()
        with origen_tab4:
            col1_m.markdown(
                f"""
                            <div style="text-align: center">
                            <h4>📮Los datos recopilados a partir de los registros
                            de un {familia_selected}, indican que esta familia de software malicioso
                            ha visto mayor prescencia en  {selected_data["Origen"].value_counts().idxmax()}

                            <h6> Nota: Medalware clasifica los paises tomando como referencia la normativa ISO 3166-1, alpha-3
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
            color_continuous_scale="portland",
            labels={"cantidad": "Cantidad"},
            title="Distribución de Origen",
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

        fig5.update_layout(width=800, height=600)

        mapa_malwares = st.container()
        with mapa_malwares:
            col1_m.plotly_chart(
                fig5, config={"displaylogo": False}, use_container_width=True
            )

        tabla_familias = tab1.container()
        with tabla_familias:
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.markdown(
                f"""
            <div style="text-align: center">
            <h4> 📋⬇️Tabla de Registro de datos recopilados de {familia_selected}⬇️📋  
            """,
                unsafe_allow_html=True,
            )
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

        malware_counts = selected_data["Malware"].value_counts()

        # Mostrar el porcentaje en Streamlit

        familia_counted = len(list(selected_data["Malware"].unique()))
        tab2.markdown(
            f"""
                <div style="text-align: justify">
                <h4>🔸Basado en los análisis de Medalware, 
                la familia de malwares {familia_selected}
                esta constituida por {(familia_counted)} malwares principales
                <h5>🔸Estos malwares corresponden a: {selected_data["Malware"].unique()}
                """,
            unsafe_allow_html=True,
        )
        fig5 = px.scatter(
            selected_data,
            x="Fecha",
            y="Malware",
            color="Malware",
            labels={"Fecha": "Fecha", "Malware": "Malware"},
            title=f"🔻Malwares que conforman la Familia {familia_selected}🔻",
        )

        fig5.update_layout(width=800, height=700, title_x=0.4)

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
        # Personalizar Colores de las gráficas de torta
        colors = px.colors.qualitative.G10

        # Contar la cantidad de filas para cada Sistema operativo
        data_grouped_origen = selected_data["SO"].value_counts()
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
            width=400,
            height=200,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # Contar la cantidad de filas para cada Sistema operativo
        data_grouped_origen = selected_data["Extension"].value_counts()
        # Crear el gráfico de torta para Sistema operativo con plotly.graph_objects
        fig8 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_origen.index,
                    values=data_grouped_origen.values,
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para Sistema operativo
        fig8.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )
        fig8.update_layout(
            width=400,
            height=200,
            margin=dict(l=10, r=10, t=30, b=10),
        )
        # Contar la cantidad de filas para cada Sistema operativo
        data_grouped_origen = selected_data["Metodo de Entrega"].value_counts()
        # Crear el gráfico de torta para Sistema operativo con plotly.graph_objects
        fig9 = go.Figure(
            data=[
                go.Pie(
                    labels=data_grouped_origen.index,
                    values=data_grouped_origen.values,
                )
            ]
        )

        # Personalizar el diseño del gráfico de torta para Sistema operativo
        fig9.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=12,
            marker=dict(colors=colors, line=dict(color=colors, width=2)),
        )
        fig9.update_layout(
            width=400,
            height=200,
            margin=dict(l=10, r=10, t=30, b=10),
        )

        fig_peso = px.box(selected_data, y="Peso", labels={"y": "Peso"})
        fig_peso.update_layout(
            width=300,
            height=450,
        )

        grafica_pie = tab3.container()
        with grafica_pie:
            col1_2.plotly_chart(fig7, config={"displaylogo": False})
            col2_2.plotly_chart(fig8, config={"displaylogo": False})
            col3_2.plotly_chart(fig9, config={"displaylogo": False})
