from hydralit import HydraApp
import streamlit as st
from home_page import home_malware
from general_page import general_malware
from malware_page import type_malware
from family_page import family_malware
from family_page import family_malware
from delivery_page import delivery_malware
from file_page import file_malware
from info_page import info_medalware

if __name__ == "__main__":
    # this is the host application, we add children to it and that's it!
    app = HydraApp(
        title="MEDALWARE",
        favicon="📊",
        hide_streamlit_markers=True,
        use_navbar=True,
    )

    # add all your application classes here
    app.add_app(title="Inicio", icon="🏠", app=home_malware())
    app.add_app(title="Información General", icon="📚", app=general_malware())
    app.add_app(title="Analisis de  Malwares", icon="🔎", app=type_malware())
    app.add_app(title="Analisis de Familias", icon="🔖", app=family_malware())
    app.add_app(title="Metodos de Entregas", icon="📥", app=delivery_malware())
    app.add_app(title="Informacion", icon="🌎", app=info_medalware())
    # run the whole lot
    app.run()
