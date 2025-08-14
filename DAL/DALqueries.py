from DBConnection import *

class Queries:
    @staticmethod
    def get_table(table_name):
        queries = "SELECT * FROM " + table_name
        return DBConnection.execute_query(table_name)



