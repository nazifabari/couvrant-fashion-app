from database import SessionLocal
from models import Item, ClothingCategory, Image

db = SessionLocal()

# creating new category and adding it to the database
new_category = ClothingCategory(name="dresses")
db.add(new_category)
db.commit()

# new item creation
new_item = Item(name="Boat Neck Rouched Maxi Dress - Chocolate Torte", brand_name="Veiled", product_url = "https://veiled.com/products/boat-neck-rouched-maxi-dress-chocolate-torte", color = "Brown", 
                price = 89.60, category_id = new_category.id, external_id = "manual-001", source = "Veiled", in_stock = True, currency = "USD")
db.add(new_item)
db.commit()

new_item_image1 = Image(image_url = "https://veiled.com/cdn/shop/files/boat-neck-rouched-maxi-dress-chocolate-torte-583191.jpg?v=1778343501&width=700"
                       , item_id= new_item.id, image_type="front" , is_display_image = True, display_order = 1 )
db.add(new_item_image1)
db.commit()


new_item_image2 = Image(image_url = "https://veiled.com/cdn/shop/files/boat-neck-rouched-maxi-dress-chocolate-torte-986275.jpg?v=1778344452&width=700"
                       , item_id= new_item.id, image_type="side" , is_display_image = False, display_order = 2 )
db.add(new_item_image2)
db.commit()

new_item_image3 = Image(image_url = "https://veiled.com/cdn/shop/files/boat-neck-rouched-maxi-dress-chocolate-torte-425745.jpg?v=1778344556&width=700"
                       , item_id= new_item.id, image_type="back" , is_display_image = False, display_order = 3 )
db.add(new_item_image3)
db.commit()

    