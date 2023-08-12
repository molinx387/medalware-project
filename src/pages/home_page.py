import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from PIL import Image
from streamlit_extras.add_vertical_space import add_vertical_space


class home_malware(HydraHeadApp):
    def run(self):
        col1, col2, col3 = st.columns([2, 4, 2])
        medalware_proyect_logo = st.container()
        with medalware_proyect_logo:
            logo = Image.open("src/media/logo.png")
            col2.image(logo)

        medalware_proyect = st.container()
        with medalware_proyect:
            col2.divider()
            col2.title(
                "📊 MEDALWARE, LA WEB DE ANÁLISIS EXPLORATORIO DE DATOS DE MALWARE"
            )

            col2.markdown(
                """
            <div style="text-align: justify">
                MEDALWARE es una aplicación web de análisis exploratorio de datos de muestras
                de malware completamente en español. Esta web procesa datos de malware recientes,
                provenientes del sitio <a href="https://bazaar.abuse.ch/">MalwareBaazar</a>, 
                para extraer de ellos información relevante. A través de distintos gráficos y análisis. 
                Con Medalware, se puede llevar un seguimiento de las tendencias de las amenazas de software
                a nivel mundial, sin limitación alguna.
            </div>
            """,
                unsafe_allow_html=True,
            )
            col2.divider()

        medalware_proyect_data = st.container()
        with medalware_proyect_data:
            col2.header("📌¿QUE TIPO DE DATOS PROPORCIONA MEDALWARE?")
            col2.markdown(
                """
            <div style="text-align: justify">
            Los datos estudiados por MEDALWARE corresponden a características de muestras de malwares
            presentes en los registros de <a href="https://bazaar.abuse.ch/">MalwareBaazar</a>. Estos 
            datos pasan por un proceso de "limpieza" para luego ser almacenados en un archivo de extension
            ".csv" que se actualiza diariamente. Las columnas que conforman el archivo CSV, corresponden a los 
            siguientes campos:\n
            </div>
            """,
                unsafe_allow_html=True,
            )
            space = col2.container()
            with space:
                add_vertical_space(1)
            with col2.expander("**🔑  SHA256**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>Es un algoritmo  criptográfico que se utiliza para la verificación de la integridad de mensajes, archivos y datos.
                """,
                    unsafe_allow_html=True,
                )
            with col2.expander("**👾  MALWARE**", expanded=False):
                st.markdown(
                    f"""                <div style="text-align: justify">
                <h6>Malware es cualquier tipo de software malicioso diseñado para infiltrarse en los sistemas operativos de los dispositivos y realizar acciones sin el conocimiento del usuario.

                """,
                    unsafe_allow_html=True,
                )

            with col2.expander("**📂  FAMILIA**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>Una familia de malware es un grupo de programas maliciosos que comparten características similares. Los miembros de una familia de malware pueden tener diferentes nombres y versiones, pero comparten el mismo código base o funcionalidad.
                """,
                    unsafe_allow_html=True,
                )
            with col2.expander("**⚙️  EXTENSION**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>Es una cadena de caracteres anexada al nombre de un archivo, habitualmente predicha por un punto. Su función principal es distinguir el contenido del archivo, de modo que el sistema operativo disponga del procedimiento necesario para ejecutarlo o interpretarlo.
                """,
                    unsafe_allow_html=True,
                )
            with col2.expander("**🧱  PESO**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>Espacio que ocupa un determinado archivo en un disco.
                """,
                    unsafe_allow_html=True,
                )
            with col2.expander("**📥   METODO DE ENTREGA**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>Es la forma como el malware es llevado al usuario final y su dispositivo.
                """,
                    unsafe_allow_html=True,
                )
            with col2.expander("**💻   SISTEMA OPERATIVO**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>Es el entorno compuesto de programas informáticos que administran los recursos de una computadora, smartphone y cualquier dispositivo.
                """,
                    unsafe_allow_html=True,
                )

            with col2.expander("**🌎  ORIGEN**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>El origen refiere al país de donde provino la muestra de malware.
                """,
                    unsafe_allow_html=True,
                )
            with col2.expander("**📅  FECHA**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>Fecha de registro del malware.
                """,
                    unsafe_allow_html=True,
                )
