from hydralit import HydraApp
import streamlit as st
from home_page import home_malware
from general_page import general_malware
from malware_page import type_malware
from family_page import family_malware
from family_page import family_malware
from delivery_page import delivery_malware
from file_page import file_malware
from origin_page import origin_malware

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
    app.add_app(title="Análisis Generales", icon="📚", app=general_malware())
    app.add_app(title="Análisis de Tipos", icon="🔖", app=type_malware())
    app.add_app(title="Familias", icon="🔖", app=family_malware())
    app.add_app(title="Metodo de Entrega", icon="🔖", app=delivery_malware())
    app.add_app(title="Extencion", icon="🔖", app=file_malware())
    app.add_app(title="Origen", icon="🔖", app=origin_malware())
    # run the whole lot
    app.run()
