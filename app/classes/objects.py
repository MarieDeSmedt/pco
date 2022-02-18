import mysql.connector as connection
import os
import streamlit as st
from dotenv import load_dotenv



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
        query = "SELECT * FROM users ORDER BY id"
        try:
            self.my_cursor.execute(query)
            result = self.my_cursor.fetchall()
            
        except Exception as e:
            st.write(e)
            return e
        return result

    def create_user(self,login,password,admin):
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
        query = "UPDATE users SET login = %s, password = %s, admin = %s WHERE id = %s"
        value = (new_login, new_password, new_admin, id_to_update)
        try:
            self.my_cursor.execute(query,value)
            self.my_db.commit()
            self.my_db.close()
        except Exception as e:
            return e    
    

    def delete_user(self, id_to_delete):
        query = f"""DELETE FROM users WHERE id = {id_to_delete}"""
        try:
            self.my_cursor.execute(query)
            self.my_db.commit()
            self.my_db.close()
        except Exception as e:
            return e  



    

    