import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
st.title("PAGINA GEMERAL")

df = pd.read_csv("src/data/cleaned.csv")
mascabron = df["Familia"].value_counts().idxmax()
st.header(f"Malware mas concurrente de hoy, [{mascabron}](https://bazaar.abuse.ch/)")

