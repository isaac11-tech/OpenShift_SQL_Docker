from fastapi import FastAPI, HTTPException
from data.creating_data import CreatingData
from data_loader.dal.data_loader import Queries

app = FastAPI()

@app.post("/seed_data")
def set_data():
    try:
        CreatingData.create_table()
        CreatingData.insert_data()
        return {"message": "Seed finished"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get_table/{table_name}")
def get_table(table_name : str):
    try:
      result = Queries.get_table(table_name)
      return result
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))





