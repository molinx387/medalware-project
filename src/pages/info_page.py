import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from PIL import Image
from streamlit_extras.add_vertical_space import add_vertical_space

from streamlit_extras.mention import mention

from streamlit_extras.badges import badge



class info_medalware(HydraHeadApp):
    def run(self):
        col1, col2= st.columns([6, 8,])
        medalware_proyect_logo = st.container()
        with medalware_proyect_logo:
            logo = Image.open("src/media/captures.jpg")
            col1.image(logo)

        medalware_proyect = st.container()
        with medalware_proyect:
            col2.title(
                " 📑MEDALWARE PROJECT"
            )


            col2.markdown(
                """
            <div style="text-align: justify">
                MEDALWARE PROJECT V-1.0, es un proyecto llevado a cabo por el 
                equipo de desarrollo de software "BoaBytes". El código fuente 
                y todos los datos obtenidos por la aplicación estan disponibles
                para su libre descarga y utilización en las siguientes plataformas:
            </div>
            """,
                unsafe_allow_html=True,
            )
            col2.divider()

        medalware_proyect_data = col2.container()
        with medalware_proyect_data:
            col3, col4= st.columns([6, 6,])
            col3.header("📌GITHUB")
            inline_mention = mention(
            label="",
            icon="github",  # Twitter is also featured!
            url="https://github.com/molinx387/medalware-project",
            write=False,
            )
            col3.markdown(
                f"""
            <div style="text-align: justify">
            El codigo fuente de esta aplicación se encuentra disponible para su descargar a traves de
            la plataforma Github, que utiliza el sistema de control de versiones y sus funciones para que
            cualquiera pueda clonar los archivos correspondientes a la aplicación y generar sus propias
            versiones a traves del siguiente enlace al repositorio.
            </div>
            """,
                unsafe_allow_html=True,
            )

            space = col3.container()
            with space:
                add_vertical_space(1)
            with col3.expander("**📘Links al repositorio:**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>{inline_mention}
            <a href="https://github.com/molinx387/medalware-project">github@medalware-project</a>
                """,
                    unsafe_allow_html=True,
                )

            col4.header("📌KAGGLE")
            inline_mention = mention(
            label="",
            icon="📥",  # Twitter is also featured!
            url="https://www.kaggle.com/datasets/jumpventura/medalware-project-malware-dataset",
            write=False,
            )
            col4.markdown(
                f"""
            <div style="text-align: justify">
            Los datos extraidos y contextualizados por esta aplicación se encuentra disponible para su descargar a traves de
            la plataforma kaggle, comunidad de repositorios para el estudio y análisis de datos, para qye cualquiera pueda 
            descarlos y realizar sus propios estudios para obtener información útil.
            """,
                unsafe_allow_html=True,
            )

            space = col4.container()
            with space:
                add_vertical_space(1)
            with col4.expander("**📘Links al repositorio:**", expanded=False):
                st.markdown(
                    f"""
                <div style="text-align: justify">
                <h6>{inline_mention}
            <a href="https://www.kaggle.com/datasets/jumpventura/medalware-project-malware-dataset">kaggle@medalware-project-dataset</a>
                """,
                    unsafe_allow_html=True,
                )