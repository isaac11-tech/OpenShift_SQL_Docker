from data_loader.dal.db_connection import DBConnection
from mysql.connector import Error

class CreatingData:

    @classmethod
    def create_table(cls):
        try:
            with open("script/create_table.sql", "r") as f:
                queries = f.read()
                DBConnection.execute_non_query(queries)
                print("Data created successfully")
        except Error as e:
            print(f"Error: {e}")

    @classmethod
    def insert_data(cls):
        try:
            with open("script/insert_data.sql", "r") as f:
                queries = f.read()
                DBConnection.execute_non_query(queries)
                print("Data inserted successfully")
        except Error as e:
            print(f"Error: {e}")