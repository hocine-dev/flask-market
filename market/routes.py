from market import app,db
from flask import render_template,redirect,url_for
from market.models import Item,User
from market.forms import RegisterForm
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
@app.route('/register',methods=['GET', 'POST'])
def Register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                    email=form.email.data,
                    password_hash=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('Market'))
    return render_template('register.html', form=form)