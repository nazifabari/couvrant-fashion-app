from database import SessionLocal
from models import Item, ClothingCategory, Image
import csv



db = SessionLocal()
try:
   file =  open("data/couvrant_products.csv", encoding="utf-8-sig")
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
            
      new_item = Item(name=row["name"], brand_name=row["brand"], product_url = row["product_url"], color = row["color"], price = row["price"], 
                     category_id = result.id, external_id = row["external_id"], source = row["brand"], in_stock = True, currency = "USD")
      db.add(new_item)
      db.commit()
      db.refresh(new_item) #so object is reread from data base so we can use it's value for Image

      #make the 3 image urls into a list and loop through them
      images =  [row["image1_url"], row["image2_url"], row["image3_url"]]
      
      for i in range(len(images)):
         if (images[i] != ""):
            new_image = Image(image_url = images[i], item_id = new_item.id)
            
            if (i ==0):
               new_image.is_display_image = True;
               new_image.display_order = 1
            if(i == 1):
               new_image.is_display_image = False;
               new_image.display_order = 2
            if(i ==2):
               new_image.is_display_image = False;
               new_image.display_order = 3
            
            db.add(new_image)
            db.commit()
   



finally:
   file.close()
   db.close()
   