from fastapi import FastAPI
from fastapi import Depends
from database import SessionLocal
from models import Item

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "FastAPI is connected."}


def get_db():
    db = SessionLocal()  
    try:
        yield db          
    finally:
        db.close()       

@app.get("/items")
def get_items(db = Depends(get_db)):
    return { "items" : db.query(Item).all()}
    