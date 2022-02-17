import streamlit as st
import os

from bokeh.models import Div
from dotenv import load_dotenv

def authentication():
    
    login = st.sidebar.text_input("Login:", value="")
    password = st.sidebar.text_input("Password:", value="", type="password")

    # select our text input field and make it into a password input
    js = "el = document.querySelectorAll('.sidebar-content input')[0]; el.type = 'password';"

    # passing js code to the onerror handler of an img tag with no src
    # triggers an error and allows automatically running our code
    html = f'<img src onerror="{js}">'

    # in contrast to st.write, this seems to allow passing javascript
    div = Div(text=html)
    st.bokeh_chart(div)

    load_dotenv()

    if login and password:

        if login == os.environ['USER1'] and password == os.environ['PASSWORD1']:
            st.success('Bonjour marie')   

        elif login == os.environ['USER2'] and password == os.environ['PASSWORD2']:
            st.success('Bonjour josephine')  

        elif login == os.environ['USER3'] and password == os.environ['PASSWORD3']:
            st.success('Bonjour hatice')  
                  
        else :
           st.error("ERROR LOGIN AND PASSWORD")
