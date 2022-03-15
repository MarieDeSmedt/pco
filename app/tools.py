import streamlit as st
import os

from bokeh.models import Div
from dotenv import load_dotenv
from classes.objects import UsersCrud,ApiCall



def authentication_tool():
    """
    tool to display component for authetication
    """
    
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
    st.session_state['authenticaton_state'] = "False"
    
    if st.sidebar.button("connect"):

        if login and password:
            uc = UsersCrud()
            try:
                user = uc.get_user(login,password)
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))
            if user :
                if user[3]!=0:
                    st.session_state["role"]="admin"
                else:
                    st.session_state["role"]="user"
                st.sidebar.success('you are connected as '+ st.session_state["role"]) 
                ac = ApiCall()
                ac.get_image()
     
                st.session_state['authenticaton_state']= True     
            else:
                st.sidebar.error("ERROR LOGIN AND PASSWORD")

    
                    
       

def create_user_tool():
    """
    Create a user with a login and password
    """
    uc = UsersCrud()
    login = st.text_input("login")
    password = st.text_input("password")
    admin = st.checkbox("admin")

    if login and password:
        users_list = uc.read_users()
        if len(users_list)>0 :
            is_unique = True
            for i, user in enumerate(users_list): 
                 
                if user[1]==login and user[2]==password:
                    st.warning("This user already exist")
                    is_unique = False 
                
        if is_unique == True:
            if st.button('create user',key = 'create'):
                try:
                    uc.create_user(login, password,admin)
                    st.success("User created successfully")
                except Exception as e:
                    st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                    st.error('Error details: {}'.format(e))


def read_users_tool():
    """
    It reads the users table from the database and returns the rows
    :return: A list of dictionaries.
    """
    uc = UsersCrud()
    try:
        rows = uc.read_users()
        return rows
    except Exception as e:
        st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
        st.error('Error details: {}'.format(e))
        st.write(e)


def update_user_tool():
    """
    It takes an id, a login, a password and an admin status and updates the user with the given id
    """
    uc = UsersCrud()
    old_id = st.number_input("id user to update", step =1)
    new_login = st.text_input("New login")
    new_password = st.text_input("New password")
    new_admin = st.checkbox("New admin")

    if old_id and (new_login or new_password or new_admin):
        if st.button('update user',key = 'update'):
            try:
                uc.update_user(old_id,new_login,new_password,new_admin)
                st.success("User updated successfully")
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))


def delete_user_tool():
    """
    It takes an id as input, and delete the user with that id
    """
    uc = UsersCrud()
    old_id = st.number_input("id user to delete",step = 1)

    if old_id :
        if st.button('delete user',key = 'delete'):
            try:
                uc.delete_user(old_id)
                st.success("User deleted successfully")
            except Exception as e:
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))