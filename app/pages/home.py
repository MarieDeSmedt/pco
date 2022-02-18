import streamlit as st
from tools import authentication_tool, create_user_tool, read_users_tool, update_user_tool, delete_user_tool


def display_home():

    st.sidebar.image('./images/inprogress.png', output_format='png')


    #authentication
    authenticaton_state = authentication_tool()

    if authenticaton_state:
        st.sidebar.write('You are authenticated')
        
        with st.expander("Create a new user"):
            create_user_tool()
        
        with st.expander("Display the list of users"):
            read_users_tool()

        with st.expander("Update a user"):
            update_user_tool()

        with st.expander("Delete a user"):
            delete_user_tool()


    else:
        st.sidebar.warning('Please authenticate')


