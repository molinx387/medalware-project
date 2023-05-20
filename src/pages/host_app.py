from hydralit import HydraApp
import streamlit as st
from homepage import home_malware
from generalpage import general_malware
from malwarefamily import f_malware

if __name__ == "__main__":
    # this is the host application, we add children to it and that's it!
    app = HydraApp(
        title="MEDALWARE",
        favicon="🧑‍💻",
        hide_streamlit_markers=True,
        use_navbar=True,
        navbar_sticky=True,
    )

    # add all your application classes here
    app.add_app(title="Inicio", icon="🏠", app=home_malware())
    app.add_app(title="General", icon="🔊", app=general_malware())
    app.add_app(title="Familias", icon="🔊", app=f_malware())
    # run the whole lot
    app.run()
