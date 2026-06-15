from fastapi import FastAPI
from fastapi import Depends
from database import SessionLocal
from models import Item
from schemas import ItemCreate
from schemas import ItemResponse


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
    
    
    
@app.post("/items", response_model=ItemResponse)
def post_items(item: ItemCreate, db = Depends(get_db)):
     new_item = Item(**item.model_dump())
     db.add(new_item)
     db.commit()
     db.refresh(new_item)
     return new_item


@app.get("/items/{id}")
def get_item(id: int, db=Depends(get_db)):
    item = db.query(Item).filter(Item.id == id).first()
    return item

