import mysql.connector as connection
import os

from dotenv import load_dotenv

def connect_to_users_database():
    load_dotenv()
    HOST = os.environ['host']
    USER = os.environ['user']
    PASSWORD = os.environ['password']
    DATABASE_NAME = os.environ['database_name']


    conn = connection.connect(host=HOST, user=USER, password=PASSWORD,database=DATABASE_NAME)

    # cursor = conn.cursor(buffered=True)

    # cursor.execute("SHOW DATABASES")

    # for database in cursor:
    #     print(database)

    # conn.close()

    return conn