import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp


class delivery_malware(HydraHeadApp):
    def run(self):
        st.title("Metodo de entrega")
