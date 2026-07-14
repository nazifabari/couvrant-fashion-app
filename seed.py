from database import SessionLocal
from models import Item, ClothingCategory
import csv



db = SessionLocal()
try:
   file =  open("data/clothing_data.csv", encoding="utf-8-sig")
   data_dict = csv.DictReader(file)
   counter = 0 #limiting the rows to 200
   
   for row in data_dict:
    counter = counter + 1
    if (counter==200): break
    result = db.query(ClothingCategory).filter(ClothingCategory.name == row["category"]).first()
    
    if (result==None):
         #create new category
         new_category = ClothingCategory(name=row["category"])
         db.add(new_category)
         db.commit()
         result = db.query(ClothingCategory).filter(ClothingCategory.name == row["category"]).first() #updating result to grab category id
         
    new_item = Item(name=row["name"], brand_name=row["brand"], product_url = row["url"], color = row["color"], price = row["price"], 
                    category_id = result.id, external_id = row["external_id"], source = row["brand"], in_stock = True, currency = "USD")
    db.add(new_item)
    db.commit()
    
finally:
   file.close()
   db.close()
   