import time

import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go




st.title(" 🧑‍💻 _MEDALWARE PROJECT_")
st.text(
    """
¡Una aplicación web de analisis de datos de muestras de malware 
para estudios de seguridad informatica completamente en español!
"""
)

values = [['SHA256', 'Familia', 'Extension', 'Peso (MB)', 'Metodo de Entrega', 'Origen','Fecha'], #1st col
  ["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]


fig = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],
  header = dict(
    values = [['<b>DATOS</b><br>'],
                  ['<b>DESCRIPTION</b>']],
    line_color='white',
    fill_color='#0D1017',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values,
    line_color='white',
    fill=dict(color=['#0D1017', '#0D1017']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
])

st.write(fig)

