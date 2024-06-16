from market import db, app
from werkzeug.security import generate_password_hash
from market.models import User, Item

# Define the items to be added
items = [
    {"name": "phone", "barcode": "123456789012", "price": 9.99, "description": "A mobile phone."},
    {"name": "tablet", "barcode": "234567890123", "price": 19.99, "description": "A tablet device."},
    {"name": "pc", "barcode": "345678901234", "price": 29.99, "description": "A personal computer."},
]

users = [
    {
        "username": "user1",
        "email": "user1@example.com",
        "password_hash": generate_password_hash('password123'),
        "budget": 1000,
        "items": [
            {"name": "phone", "barcode": "123456789012", "price": 9.99, "description": "A mobile phone."},
            {"name": "tablet", "barcode": "234567890123", "price": 19.99, "description": "A tablet device."}
        ]
    },
    {
        "username": "user2",
        "email": "user2@example.com",
        "password_hash": generate_password_hash('password123'),
        "budget": 1000,
        "items": [
            {"name": "pc", "barcode": "345678901234", "price": 29.99, "description": "A personal computer."}
        ]
    },
    {
        "username": "user3",
        "email": "user3@example.com",
        "password_hash": generate_password_hash('password123'),
        "budget": 1000,
        "items": []
    }
]

# Add the items and users to the database
with app.app_context():
    # Add items
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

    # Add users and associate items
    for user_data in users:
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            password_hash=user_data["password_hash"],
            budget=user_data["budget"]
        )
        db.session.add(user)
        db.session.commit()  # Commit user first to get user ID

        # Add associated items
        for item_data in user_data["items"]:
            item = Item.query.filter_by(barcode=item_data["barcode"]).first()
            if item:
                item.owner = user.id  # Assign the owner to the item
                db.session.add(item)
    db.session.commit()
    print("Users and their items added to the database.")
