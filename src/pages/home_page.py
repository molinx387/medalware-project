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
            MEDALWARE  es una aplicacion web de analisis exploratorio de datos de muestras de malware completamente en español, 
            que procesa datos de malware recientes del sitio [MalwareBaazar](https://bazaar.abuse.ch/), para extraer 
            de ellos y en tiempo real informacion relevante, a traves de distintos graficos y analisis. Con Medalware, se puede llevar un seguimiento 
            de las tendencias de este tipo de software a nivel mundial, en aspectos como:
            Metodos de distribucion, Extensiones de archivos, Familias, Origenes conocidos, entre otros.
                """
            )
