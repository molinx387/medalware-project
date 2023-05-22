import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp
from PIL import Image
from streamlit_extras.colored_header import colored_header


class home_malware(HydraHeadApp):
    def run(self):
        medalware_proyect = st.container()
        with medalware_proyect:
            col1, col2, col3 = st.columns([2, 4, 2])
            #col4, col5 = st.columns([9, 0.1])

            col2.title("📊MEDALWARE PROJECT📊")
            col2.subheader(' "Web de analisis explotario de datos de malware"')
            
            
            #("<h3 style='text-align: center;'> 'Una web de analisis explotario de datos de malware'</h3>", unsafe_allow_html=True)
            
            
            st.markdown(
            """
            <div style="text-align: justify">
                MEDALWARE es una aplicación web de análisis exploratorio de datos de muestras de malware completamente en español, 
                que procesa datos de malware recientes del sitio <a href="https://bazaar.abuse.ch/">MalwareBaazar</a>, para extraer 
                de ellos y en tiempo real información relevante, a través de distintos gráficos y análisis. Con Medalware, se puede llevar un seguimiento 
                de las tendencias de este tipo de software a nivel mundial, en aspectos como:
                Métodos de distribución, Extensiones de archivos, Familias, Orígenes conocidos, entre otros.
            </div>
            """,
            unsafe_allow_html=True
        )
