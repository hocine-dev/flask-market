from market import app,db
from flask import render_template,redirect,url_for,flash
from market.models import Item,User
from market.forms import RegisterForm,LoginForm
from flask_login import login_user
@app.route('/')
@app.route('/home')
def Home():
    return render_template('index.html')

@app.route('/market')

def Market():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/login',methods=['GET', 'POST'])
def Login():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'success,you are logged in as {attempted_user.username}',category='success')
            return redirect(url_for('Market'))
        else:
            flash('error in login data, please try again!',category='danger')
        
    return render_template('login.html',form=form)


@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('Market'))
    
    if form.errors:
        for err_msgs in form.errors.values():
            for err_msg in err_msgs:
                flash(f'{err_msg}', 'danger')
    
    return render_template('register.html', form=form)
