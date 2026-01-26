from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from db import database 

models.Base.metadata.create_all(bind=database.motor)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def inicio():
    return {f""}