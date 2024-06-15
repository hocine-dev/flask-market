from market import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False,unique=True)
    description = db.Column(db.String(1024), nullable=False)
    barcode = db.Column(db.Integer, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)