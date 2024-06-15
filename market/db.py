from market import app, db
from models import Item

with app.app_context():
    db.create_all()
    print("Database tables created.")
