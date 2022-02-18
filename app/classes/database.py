import mysql.connector as connection
import os
import streamlit as st
from dotenv import load_dotenv

# def connect_to_users_database():

#     load_dotenv()
#     HOST = os.environ['host']
#     USER = os.environ['user']
#     PASSWORD = os.environ['password']
#     DATABASE_NAME = os.environ['database_name']
#     conn = connection.connect(host=HOST, user=USER, password=PASSWORD,database=DATABASE_NAME)

#     return conn

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
    
    def __del__(self):
        self.my_db.commit()



class UsersCrud(Database):
   
    
    def read_users(self):        
        query = "SELECT * FROM users ORDER BY id"
        try:
            self.my_cursor.execute(query)
            result = self.my_cursor.fetchall()
        except Exception as e:
            st.write(e)
            return e
        return result

    # def create_user(cls,login,password,admin):
    #     query = "INSERT INTO `users` (`id`, `login`, `password`, `admin`) VALUES (NULL, %s, %s, %s)"
    #     value = (login, password,admin)
    #     try:
    #         cls.my_cursor.execute(query,value)
    #     except Exception as e:
    #         return e
        
   

    # def update_user(self,id_to_update,new_login,new_password,new_admin):
    #     query = "UPDATE users SET login = %s, password = %s, admin = %s WHERE id = %s"
    #     value = (new_login, new_password, new_admin, id_to_update)
    #     try:
    #         self.my_cursor.execute(query,value)
    #     except Exception as e:
    #         return e    
    

    # def delete_user(self, id_to_delete):
    #     query = f"""DELETE FROM users WHERE id = {id_to_delete}"""
    #     try:
    #         self.my_cursor.execute(query)
    #     except Exception as e:
    #         return e  



    

    