from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List


class ImageResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  image_url: str
  item_id: int
  image_type: str
  is_display_image : bool
  display_order: int


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
  model_config = ConfigDict(from_attributes=True)
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
  images: List[ImageResponse]


class ItemsResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  items: List[ItemResponse]
  total: int