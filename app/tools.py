import streamlit as st
import os

from bokeh.models import Div
from dotenv import load_dotenv
from database import connect_to_mysql as ctm
from database import users_crud as uc


def authentication_tool():

    #con=ctm.connect_to_users()
    
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
    authenticaton_state = False

    if login and password:

        authenticaton_state = True

        if login == os.environ['USER1'] and password == os.environ['PASSWORD1']:
            st.success('attention connectée en dur')   
            
        elif login == os.environ['USER2'] and password == os.environ['PASSWORD2']:
            st.success('attention connectée en dur')   

        elif login == os.environ['USER3'] and password == os.environ['PASSWORD3']:
            st.success('attention connectée en dur')  
                  
        else :
           st.error("ERROR LOGIN AND PASSWORD")
           authenticaton_state = False
           

    return authenticaton_state

def create_user_tool():

    login = st.text_input("login")
    password = st.text_input("password")
    admin = st.checkbox("admin")

    if login and password:

        if st.button('create user'):
            try:
                connection = ctm.connect_to_users_database()
                uc.create_user(login,password,admin,connection)
                st.success("User created successfully")
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))

def read_users_tool():
    try:
        connection = ctm.connect_to_users_database()
        rows = uc.read_users(connection)
        for user in rows:
            if user[3] == 1:
                st.write("Id:" + str(user[0]) + "login: " + user[1] + ", pasword: " + user[2] + ", Is admin: yes")
            else:
                st.write("Id:" + str(user[0]) + "login: " + user[1] + ", pasword: " + user[2] + ", Is admin: no")
            st.write("-----------------------------------")

    except Exception as e:
        st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
        st.error('Error details: {}'.format(e))

def update_user_tool():
    old_id = st.number_input("id user to update", step =1)
    new_login = st.text_input("New login")
    new_password = st.text_input("New password")
    new_admin = st.checkbox("New admin")

    if old_id and new_login and new_password:

        if st.button('update user'):
            try:
                connection = ctm.connect_to_users_database()
                uc.update_user(connection, old_id,new_login,new_password,new_admin)
                connection2 = ctm.connect_to_users_database()
                uc.read_users(connection2)
                st.success("User updated successfully")
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))



def delete_user_tool():
    old_id = st.number_input("id user to delete",step = 1)
    if old_id :

        if st.button('delete user'):
            try:
                connection = ctm.connect_to_users_database()
                uc.delete_user(connection, old_id)
                connection2 = ctm.connect_to_users_database()
                uc.read_users(connection2)
                st.success("User deleted successfully")
            except connection.errors as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))