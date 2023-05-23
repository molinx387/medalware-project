from hydralit import header
import pandas as pd 
import streamlit as st
df = pd.read_csv("src/data/malwares.csv")
header_list = list(df.columns)
print(header_list)
import plotly.graph_objects as go

values = [header_list, #1st col
  ["Es un algoritmo  criptográfico que se utiliza para la verificación de la integridad de mensajes, archivos y datos.",
  "Una familia de malware es un grupo de programas maliciosos que comparten características similares. Los miembros de una familia de malware pueden tener diferentes nombres y versiones, pero comparten el mismo código base o funcionalidad.",
  "Es una cadena de caracteres anexada al nombre de un archivo, habitualmente predicha por un punto. Su función principal es distinguir el contenido del archivo, de modo que el sistema operativo disponga del procedimiento necesario para ejecutarlo o interpretarlo",
  "Espacio que ocupa un determinado archivo en un disco.",
  "Es la forma como el malware es llevado al usuario final y su dispositivo",
  "El origen refiere al pais de donde provino la muestra de malware",
  "El dia en el que la muestra de malware fue registrada en Medalware",
   "La hora exacta en la que la muestra fue registrada en Medalware"]
    ]

fig = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],
  header = dict(
    values = [['<b>EXPENSES</b><br>as of July 2017'],
                  ['<b>DESCRIPTION</b>']],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
])
fig.show()
