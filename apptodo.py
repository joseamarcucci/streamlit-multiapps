import streamlit as st
import sys
import os
import usuarios0
import usuarios
from multiapp import MultiApp

#import multiapp2 

import home, data_stats,mayo,meses,home5,moodle5,todas0,todasu,moodle,abril25,graba,febrero,marzo,abril,home4,home2,moodle2,moodle4,usuarios,usuarios0,usuariosbbc # import your app modules here


st.set_page_config(
page_title="USAL Uso plataformas Blackboard",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide",
initial_sidebar_state="expanded",)
app = MultiApp()

# Add all your application here

#st.sidebar.markdown("<h3 style='text-align: left; color: black;font-weight:500;'>Blackboard Collaborate y ULTRA</h3>", unsafe_allow_html=True)
app.add_app("Blackboard Collaborate:", todasu.app)
app.add_app("Reporte gral y mensual", meses.app)
app.add_app("Febrero", febrero.app)
app.add_app("Campus BBLearn ", home2.app)
app.add_app("Campus Moodle ", moodle2.app)
app.add_app("Marzo", marzo.app)
app.add_app("Campus BBLearn", home.app)
app.add_app("Campus Moodle ", moodle.app)
app.add_app("Abril", abril.app)
#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
app.add_app("Campus BBLearn", home4.app)
app.add_app("Campus Moodle", moodle4.app)
app.add_app("Mayo", mayo.app)
#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
app.add_app("Campus BBLearn", home5.app)
app.add_app("Campus Moodle", moodle5.app)
app.add_app("Grabaciones", graba.app)
#app.add_app("Usuarios Collaborate", usuariosbbc.app)
app.add_app("Blackboard ULTRA:", todasu.app)
app.add_app("Usuarios del campus por UA", usuarios.app)
app.add_app("Usuarios totales del campus", usuarios0.app)
#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
#app.add_app("Datos x UA", todas.app)




app.run()

#PAGES = {
#    "Blackboard ULTRA:": todas0,
 #   "Usuarios del campus por UA": usuarios,
 #   "Usuarios totales del campus": usuarios0
#}
#st.sidebar.title('Navigation')
#election = st.sidebar.radio("", list(PAGES.keys()))
#page = PAGES[selection]
#page.app()

   
#app = MultiApp2()

#app.run()

