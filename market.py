from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def Home():
    return render_template('index.html')

@app.route('/market')

def Market():
    items = [
    {
        "id": 1,
        "name": "phone",
        "barcode": "123456789012",
        "price": 9.99
    },
    {
        "id": 2,
        "name": "tablet",
        "barcode": "234567890123",
        "price": 19.99
    },
    {
        "id": 3,
        "name": "pc",
        "barcode": "345678901234",
        "price": 29.99
    }
]
    return render_template('market.html',items=items)

@app.route('/login')
def Login():
    return render_template('index.html')
@app.route('/register')
def Register():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
