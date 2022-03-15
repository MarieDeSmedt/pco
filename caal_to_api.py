import streamlit as st
import requests


if selection == "display a client":
        input_id = st.number_input('enter the client id to display')
        if input_id > 0:
            input_id = int(input_id)
            #display_client_by_id(input_id)
            response = requests.get(" http://127.0.0.1:8000/clients/{}".format(input_id))
            if not response:
                st.write('No Data!')
            else:
                client = response.json()
                st.write('Name: ', client['name'])
                st.write('Firstname: ', client['firstname'])
                st.write('Information: ', client['info'])