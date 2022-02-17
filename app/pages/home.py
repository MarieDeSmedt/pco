import streamlit as st
from tools import authentication
from admin import display_admin

def display_home():

    st.sidebar.image('./images/inprogress.png', output_format='png')


    #authentication
    authenticaton_state = authentication()

    if authenticaton_state:
        st.sidebar.write('vous etes authentifié')
        
        

    else:
        st.sidebar.warning('merci de vous authentifier')


