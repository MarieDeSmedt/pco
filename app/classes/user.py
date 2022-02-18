import streamlit as st
from classes.database  import Database


# def create_user(login,password,admin,connection):
#     query = "INSERT INTO `users` (`id`, `login`, `password`, `admin`) VALUES (NULL, %s, %s, %s)"
#     value = (login, password,admin)
#     cursor = connection.cursor()
#     cursor.execute(query, value)
#     connection.commit()
#     connection.close()
    

# def read_users(connection):
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM `users`")
#     rows = cursor.fetchall()
#     connection.close()
#     return rows


# def update_user(connection,id_to_update,new_login,new_password,new_admin):
#     cursor = connection.cursor()   
#     query = "UPDATE users SET login = %s, password = %s, admin = %s WHERE id = %s"
#     value = (new_login, new_password, new_admin, id_to_update)
#     cursor.execute(query,value)
#     connection.commit()
#     connection.close()
    

# def delete_user(connection, id_to_delete):
#     cursor = connection.cursor()   
#     query = f"""DELETE FROM users WHERE id = {id_to_delete}"""
#     cursor.execute(query)
#     connection.commit()
#     connection
#     connection.close()


