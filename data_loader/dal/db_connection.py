import mysql.connector
from mysql.connector import Error
import os


class DBConnection:

    @staticmethod
    def connect(cs=None):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                user="myuser",
                password="mypassword",
                database="mydb"
            ) if cs is None else mysql.connector.connect(**cs)

            if conn.is_connected():
                return conn
        except Error as e:
            print(f"Error: {e}")
            return None


    @staticmethod
    def disconnect(conn):
        if conn.is_connected():
            conn.close()

    @staticmethod
    def execute_query(sql, params=None, cs=None):
        conn = DBConnection.connect(cs)
        cursor = None

        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.fetchall()

        except Exception as e:
            print(f"Query error: {e}")
            return None

        finally:
            if cursor:
             cursor.close()
            DBConnection.disconnect(conn)




    @staticmethod
    def execute_non_query(sql, params=None, cs=None):
        conn = DBConnection.connect(cs)
        cursor = None

        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Query error: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            DBConnection.disconnect(conn)



