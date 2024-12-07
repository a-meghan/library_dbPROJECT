import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "my_library"
    user = "root"
    password = "Dak0ta2023!"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        if conn.is_connected():
            print("Connected to MySQL database successfully")
            cursor = conn.cursor()
            return conn, cursor

    except Error as e:
        print(f"Error: {e}")