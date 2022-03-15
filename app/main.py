
import streamlit as st
import hydralit_components as hc
import pandas as pd

from pages.home import display_home
from pages.admin import display_admin
from tools import *



# toujours en premier
st.set_page_config(layout='wide',initial_sidebar_state='expanded')

#css
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 0rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

#init
st.session_state['authenticaton_state']= False
st.session_state["role"]="user"

#connexion
authentication_tool()


#si connecté
if st.session_state['authenticaton_state']:

  
    #Nom des onglets
    if st.session_state["role"] == "admin":
        menu_data = [
            {'label':"Home"},
            {'label':"Admin"}
        ]
    else:
        menu_data = [
            {'label':"Home"}
        ]

    #set the navbar
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        sticky_nav=True, 
        sticky_mode='pinned'
    )


    #action selon onglet 
    if menu_id == "Admin":
        display_admin()
    else: 
        display_home()


else:
    st.warning("Please connect")
    



    