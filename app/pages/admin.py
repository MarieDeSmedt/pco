import streamlit as st
from tools import *



def display_admin():    
    
        
        with st.expander("Create a new user"):
            create_user_tool()
        
        with st.expander("Display the list of users"):
            read_users_tool()

        with st.expander("Update a user"):
            update_user_tool()

        with st.expander("Delete a user"):
            delete_user_tool()
