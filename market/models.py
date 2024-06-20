from market import db,b_crypt


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False,unique=True)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False,default=1000)
    items = db.relationship('Item',backref='owned_user',lazy=True)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = b_crypt.generate_password_hash(plain_text_password).decode('utf-8')
    




class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False,unique=True)
    description = db.Column(db.String(1024), nullable=False)
    barcode = db.Column(db.Integer(), unique=True, nullable=False)
    price = db.Column(db.Float(), nullable=False)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))
    