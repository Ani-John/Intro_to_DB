import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # CONNECT TO MYSQL SERVER
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="master1"   # <-- replace with your real password
        )

        if mydb.is_connected():
            cursor = mydb.cursor()

            # CREATE DATABASE (IF NOT EXISTS)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        # ALWAYS CLOSE THE CONNECTION
        try:
            cursor.close()
            mydb.close()
        except:
            pass


if __name__ == "__main__":
    create_database()

