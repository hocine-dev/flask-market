from market import app
from flask import render_template
from market.models import Item
@app.route('/')
@app.route('/home')
def Home():
    return render_template('index.html')

@app.route('/market')

def Market():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/login')
def Login():
    return render_template('index.html')
@app.route('/register')
def Register():
    return render_template('index.html')