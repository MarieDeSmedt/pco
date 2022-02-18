import streamlit as st
import os

from bokeh.models import Div
from dotenv import load_dotenv
from classes.database import UsersCrud 



def authentication_tool():
    
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
        if st.sidebar.button("connect"):
            authenticaton_state = True
            uc= UsersCrud()
            users_list = uc.read_users()
            if len(users_list)>0 :
                for user in users_list:            
                    if user[1]==login and user[2]==password:
                        if user[3]:
                            st.session_state["role"]="admin"
                        else:
                            st.session_state["role"]="user"
                        st.sidebar.success('Vous êtes connecté en tant que '+ st.session_state["role"])       
            else :
                st.sidebar.error("ERROR LOGIN AND PASSWORD")
            authenticaton_state = False
           
    return authenticaton_state

def create_user_tool():

    login = st.text_input("login")
    password = st.text_input("password")
    admin = st.checkbox("admin")

    if login and password:
        if st.button('create user'):
            uc = UsersCrud()
            try:
                uc.create_user(login, password,admin)
                st.success("User created successfully")
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))

def read_users_tool():
    uc = UsersCrud()
    try:
        rows = uc.read_users()
        for user in rows:
            if user[3] == 1:
                st.write("Id:" + str(user[0]) + "   login: " + user[1] + ",  pasword: " + user[2] + ",  Is admin: yes")
            else:
                st.write("Id:" + str(user[0]) + "   login: " + user[1] + ",  pasword: " + user[2] + ",  Is admin: no")
            st.write("-----------------------------------")

    except Exception as e:
        st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
        st.error('Error details: {}'.format(e))
        st.write(e)

def update_user_tool():

    old_id = st.number_input("id user to update", step =1)
    new_login = st.text_input("New login")
    new_password = st.text_input("New password")
    new_admin = st.checkbox("New admin")

    if old_id and new_login and new_password:
        if st.button('update user'):
            uc = UsersCrud()
            try:
                uc.update_user(old_id,new_login,new_password,new_admin)
                st.success("User updated successfully")
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))

def delete_user_tool():

    old_id = st.number_input("id user to delete",step = 1)

    if old_id :
        if st.button('delete user'):
            uc = UsersCrud()
            try:
                uc.delete_user(old_id)
                st.success("User deleted successfully")
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))