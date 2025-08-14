import mysql.connector
from mysql.connector import Error


class DBConnection:

    @staticmethod
    def connect(cs=None):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='eagleeyedb'
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
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()
            DBConnection.disconnect(conn)

    @staticmethod
    def print_results(results):
        if not results:
            print("No results found.")
            return

        for row in results:
            for key, value in row.items():
                print(f"{key}: {value}")
            print("---")
