import mysql.connector as connection
import os
import streamlit as st
from dotenv import load_dotenv
import requests



class Database:

    load_dotenv()

    def __init__(self):
        
        self.my_db = connection.connect(
            host=os.environ['host'],
            user=os.environ['user'],
            password=os.environ['password'],
            database=os.environ['database_name']
        )
        self.my_cursor = self.my_db.cursor() 


class UsersCrud(Database):
    
    def read_users(self):        
        """
        It reads all the users from the database.
        :return: A list of tuples.
        """
        query = "SELECT * FROM users ORDER BY id"
        try:
            self.my_cursor.execute(query)
            result = self.my_cursor.fetchall()
            
        except Exception as e:
            st.write(e)
            return e
        return result

    def create_user(self,login,password,admin):
        """
        It creates a user in the database.
        
        :param login: The username of the user
        :param password: The password of the user
        :param admin: A boolean value indicating whether the user is an admin or not
        :return: Nothing is being returned.
        """
        query = "INSERT INTO `users` (`id`, `login`, `password`, `admin`) VALUES (NULL, %s, %s, %s)"
        value = (login, password,admin)
        try:
            st.write(query)
            st.write(value)
            self.my_cursor.execute(query,value)
            self.my_db.commit()
            self.my_db.close()
        except Exception as e:
            return e

    def update_user(self,id_to_update,new_login,new_password,new_admin):
        """
        The function takes in the id of the user to update, the new login, new password, and new admin
        status. 
        It then updates the user's login, password, and admin status in the database.
        
        :param id_to_update: The id of the user you want to update
        :param new_login: The new login of the user
        :param new_password: The new password for the user
        :param new_admin: a boolean value (True or False) that represents whether the user is an admin
        or not
        :return: Nothing.
        """
        query = "UPDATE users SET login = %s, password = %s, admin = %s WHERE id = %s"
        value = (new_login, new_password, new_admin, id_to_update)
        try:
            self.my_cursor.execute(query,value)
            self.my_db.commit()
            self.my_db.close()
        except Exception as e:
            return e    
    
    def delete_user(self, id_to_delete):
        """
        Delete a user from the database
        
        :param id_to_delete: The id of the user you want to delete
        :return: Nothing.
        """

        query = f"""DELETE FROM users WHERE id = {id_to_delete}"""
        try:
            self.my_cursor.execute(query)
            self.my_db.commit()
            self.my_db.close()
        except Exception as e:
            return e  

    def get_user(self,login,password):
        """
        Get the user from the database
        
        :param login: The user's login name
        :param password: The password to be used to login
        :return: A list of the user's information.
        """

        uc= UsersCrud()
        users_list = uc.read_users()
        if len(users_list)>0 :
            for user in users_list:            
                if user[1]==login and user[2]==password:
                    return user


class ApiCall:

    def get_image(self):
        response = requests.get(" https://dog.ceo/api/breeds/image/random")
        if not response:
            st.write('No Data!')
        else:
            st.sidebar.image(response.json()['message'])