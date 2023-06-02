import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp


class delivery_malware(HydraHeadApp):
    def run(self):
        data = pd.read_csv("src/data/malwares.csv")
        title = st.container()
        with title:
            col1, col2 = st.columns([6,5])
            col1.title('ANALISIS DE METODOS DE ENTREGA DE MALWARE')
            col2.image("src/media/method.png")




        tag_selector = st.container()
        with tag_selector:
            tab1, tab2, tab3,tab4 = st.tabs(
                [
                    "       📈",
                    "       🪬Familia",
                    "       📊Caracteristicas",
                    "       🌎Origen",
                ]
            )

