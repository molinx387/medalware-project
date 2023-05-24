import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from PIL import Image


class home_malware(HydraHeadApp):
    def run(self):
        medalware_proyect = st.container()
        with medalware_proyect:
            col1, col2, col3 = st.columns([2, 4, 2])
            col4, col5,col6,col7, = st.columns([2.5,2.5,2.5,2.5])
            col8,col9,col10 = st.columns([3.33,3.33,3.33])
            # col2.title("📊MEDALWARE PROJECT📊")

            logo = Image.open('src/media/logo.png')
            col1.header(" 👀 👇")
            col2.image(logo)
            col2.divider()
            col2.title("📊 MEDALWARE, LA WEB DE ANÁLISIS EXPLORATORIO DE DATOS DE MALWARE")
 
 
            col2.markdown(
            """
            <div style="text-align: justify">
                MEDALWARE es una aplicación web de análisis exploratorio de datos de muestras
                de malware completamente en español. Esta web procesa datos de malware recientes,
                provenientes del sitio <a href="https://bazaar.abuse.ch/">MalwareBaazar</a>, 
                para extraer de ellos información relevante. A través de distintos gráficos y análisis. 
                Con Medalware, se puede llevar un seguimiento de las tendencias de las amenazas de software
                a nivel mundial, sin limitacion alguna.
            </div>
            """,
            unsafe_allow_html=True)
            col2.divider()
            col2.header("📌¿QUE TIPO DE DATOS PROPORCIONA MEDALWARE?")
            col2.markdown(
            """
            <div style="text-align: justify">
            Los datos estudiados por MEDALWARE corresponden a caracteristicas de muestras de malwares
            presentes en los registros de <a href="https://bazaar.abuse.ch/">MalwareBaazar</a>. Estos 
            datos pasan por un proceso de "limpieza" para luego ser almacenados en un archivo de extension
            ".csv" que se actualiza diariamente. Las columnas que conforman el archivo CSV, corresponden a los 
            siguientes campos:\n
            </div>
            """,
            unsafe_allow_html=True)
            info_data = {
                         '🏷SHA256': "Es un algoritmo  criptográfico que se utiliza para la verificación de la integridad de mensajes, archivos y datos.",
                         '🧬Familia': "Una familia de malware es un grupo de programas maliciosos que comparten características similares. Los miembros de una familia de malware pueden tener diferentes nombres y versiones, pero comparten el mismo código base o funcionalidad.",
                         '⚙️Extension' : "Es una cadena de caracteres anexada al nombre de un archivo, habitualmente predicha por un punto. Su función principal es distinguir el contenido del archivo, de modo que el sistema operativo disponga del procedimiento necesario para ejecutarlo o interpretarlo",
                         '📥Peso' : "Espacio que ocupa un determinado archivo en un disco.",
                         '🪤Metood de Entrega' : "Es la forma como el malware es llevado al usuario final y su dispositivo",
                         '🌎Origen' : "El origen refiere al pais de donde provino la muestra de malware",
                         '📆Dia' : "El dia en el que la muestra de malware fue registrada en Medalware",
                         '⏰Hora' : "La hora exacta en la que la muestra fue registrada en Medalware"
            }
            items = {'item 1': 'description 1', 'item 2': 'description 2', 'item 3': 'description 3'}
            col2.subheader(body='')
            for item, description in info_data.items():
                col2.markdown(f' >**:red[</{item}>]** **:** {description}')

            col2.divider()
            col2.header("🎂Feliz Cumpleaños compita Jose")
            from streamlit_extras.let_it_rain import rain

            rain(
                    emoji="🎉",
                    font_size=60,
                    falling_speed=4,
                    animation_length="infinite",
                )

