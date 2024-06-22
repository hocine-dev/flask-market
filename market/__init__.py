from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '0x769f6de692'
db = SQLAlchemy(app)
b_crypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "Login"
login_manager.login_message_category = "info"



from market import routes
from market import models