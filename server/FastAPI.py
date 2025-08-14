import uvicorn
from fastapi import FastAPI
from DAL import DALqueries

app = FastAPI()

@app.get("/get_table")
def get_table():
    result = get_table()
    return result




