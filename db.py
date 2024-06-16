from market import app, db
from market.models import User,Item

with app.app_context():
    db.create_all()
    print("Database tables created.")
