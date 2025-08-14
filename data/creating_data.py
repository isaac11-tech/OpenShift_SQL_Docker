from DAL.DBConnection import DBConnection
from mysql.connector import Error

class CreateData:

    @staticmethod
    def create_table():
        try:
            queries = open("script/create_table.sql", "r")
            DBConnection.execute_query(queries)
        except Error as e:
            print(f"Error: {e}")

    @staticmethod
    def insert_data():
        try:
            queries = open("script/insert_data.sql", "r")
            DBConnection.execute_query(queries)
        except Error as e:
            print(f"Error: {e}")

