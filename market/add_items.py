from market import db,app
from models import Item
# Define the items to be added
items = [
    {"name": "phone", "barcode": "123456789012", "price": 9.99, "description": "A mobile phone."},
    {"name": "tablet", "barcode": "234567890123", "price": 19.99, "description": "A tablet device."},
    {"name": "pc", "barcode": "345678901234", "price": 29.99, "description": "A personal computer."},
]

# Add the items to the database
with app.app_context():
    for item_data in items:
        item = Item(
            name=item_data["name"],
            barcode=item_data["barcode"],
            price=item_data["price"],
            description=item_data["description"]
        )
        db.session.add(item)
    db.session.commit()
    print("Items added to the database.")
