import uvicorn
from data import creating_data



#this mead for the user do get the table
if __name__ == "__main__":
     creating_data.insert_data()# creating table to the sql server
     creating_data.create_table()#insert data to the sql table
     uvicorn.run("FastAPI:app", host="127.0.0.1", port=8000, reload=True)