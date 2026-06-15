from pydantic import BaseModel
from datetime import datetime

class ItemCreate(BaseModel):
  name: str 
  description: str
  price: float
  currency: str
  brand_name: str 
  product_url : str
  color : str
  category_id: int
  in_stock: bool
  source : str
  external_id : str


class ItemResponse(BaseModel):
  id: int 
  created_at : datetime
  name: str 
  description: str
  price: float
  currency: str
  brand_name: str 
  product_url : str
  color : str
  category_id: int
  in_stock: bool
  source : str
  external_id : str
  