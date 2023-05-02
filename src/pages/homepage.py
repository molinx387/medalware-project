import time

import pandas as pd
import streamlit as st

st.title(" 🧑‍💻 _MEDALWARE PROJECT_")
st.text(
    """
¡Una aplicación web de analisis de datos de muestras de malware 
para estudios de seguridad informatica completamente en español!
"""
)
df = pd.read_csv("../data/cleaned.csv")
mascabron = df["Familia"].value_counts().idxmax()
st.header(f"Malware mas concurrente de hoy, [{mascabron}](https://bazaar.abuse.ch/)")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
