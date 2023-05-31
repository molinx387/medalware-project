from hydralit import HydraApp
import streamlit as st
from home_page import home_malware
from general_page import general_malware
from malware_family import familia_malware

if __name__ == "__main__":
    
    # this is the host application, we add children to it and that's it!
    app = HydraApp(
        title="MEDALWARE",
        favicon="📊",
        hide_streamlit_markers=True,
        use_navbar=True,
        navbar_sticky=True,
    )

    # add all your application classes here
    app.add_app(title="Inicio", icon="🏠", app=home_malware())
    app.add_app(title="Análisis Generales", icon="📚", app=general_malware())
    app.add_app(title="Análisis de Tipos", icon="🔖", app=familia_malware())
    # run the whole lot
    app.run()
