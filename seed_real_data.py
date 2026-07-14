from database import SessionLocal
from models import Item, ClothingCategory, Image

db = SessionLocal()

# attaching new item with an already existing category
category = db.query(ClothingCategory).filter(ClothingCategory.name == "dresses").first()

# new item creation
new_item = Item(name="LONG LACE DRESS", brand_name="Gracieuse", product_url = "https://www.gracieuseparis.com/products/yellow-lace-dress?variant=53571669131601", color = "White", 
                price = 77.00, category_id = category.id, external_id = "manual-003", source = "Gracieuse", in_stock = True, currency = "USD")
db.add(new_item)
db.commit()

new_item_image1 = Image(image_url = "https://www.gracieuseparis.com/cdn/shop/files/magnific_prompt-positif-use-img1-o_5xe6VylKxe_1.png?v=1780339743&width=1400"
                       , item_id= new_item.id, image_type="front" , is_display_image = True, display_order = 1 )
db.add(new_item_image1)
db.commit()


new_item_image2 = Image(image_url = "https://www.gracieuseparis.com/cdn/shop/files/magnific_prompt-positif-use-img1-a_2987555943.png?v=1778840566&width=1400"
                       , item_id= new_item.id, image_type="back" , is_display_image = False, display_order = 2 )
db.add(new_item_image2)
db.commit()










    