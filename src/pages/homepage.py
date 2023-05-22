import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
from hydralit import HydraHeadApp


class home_malware(HydraHeadApp):
    def run(self):
        medalware_proyect = st.container()
        with medalware_proyect:
            st.title("🧑‍💻 _MEDALWARE PROJECT_")
            st.text(
                """
            ¡Una aplicación web de analisis de datos de muestras de malware para estudios de seguridad informatica completamente en español!
            """
            )

        values = [
            [
                "SHA256",
                "Familia",
                "Extension",
                "Peso (MB)",
                "Metodo de Entrega",
                "Origen",
                "Fecha",
            ],  # 1st col
            [
                "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
            ],
        ]
                
        fig = go.Figure(
            data=[
                go.Table(
                    columnorder=[1, 2],
                    columnwidth=[80, 400],
                    header=dict(
                        values=[["<b>DATOS</b><br>"], ["<b>DESCRIPTION</b>"]],
                        line_color="#8ec07c",
                        fill_color="#3c3836",
                        align=["left", "center"],
                        font=dict(color="white", size=14, family="Source Code Pro"),
                        height=40,
                    ),
                    cells=dict(
                        values=values,
                        line_color="#8ec07c",
                        fill=dict(color=["#3c3836", "#282828"]),
                        align=["left", "center"],
                        font=dict(color="#ebdbb2", size=14, family="Source Code Pro"),  # Cambia la fuente aquí
                        height=30,
                    ),
                )
            ]
        )
        datos_medalware = st.container()
        with datos_medalware:
            st.subheader("Tabla de Datos")
            col1, col2, col3 = st.columns([0.1, 4, 0.1])
            col2.write(fig)
