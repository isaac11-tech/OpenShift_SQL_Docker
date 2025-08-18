from db_connection import *

class Queries:

    @classmethod
    def get_table(cls,table_name):
        queries = "SELECT * FROM " + table_name
        return DBConnection.execute_query(queries)



