from market import app,db
from flask import render_template,redirect,url_for,flash,request
from market.models import Item,User
from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
from flask_login import login_user,logout_user,login_required,current_user
@app.route('/')
@app.route('/Logout')
def Logout():
    logout_user()
    flash(f'you have been logged out',category='info')
    return redirect(url_for('Home'))
    


@app.route('/home')
def Home():
    return render_template('index.html')

@app.route('/market',methods=['GET', 'POST'])
@login_required
def Market():
    purchaseItemForm = PurchaseItemForm()
    sellItemForm = SellItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_obj = Item.query.filter_by(name=purchased_item).first()
        if p_item_obj:
            if current_user.budget > p_item_obj.price:
                p_item_obj.buy(current_user)
                flash(f'success,you have bought {p_item_obj.name} for {p_item_obj.price}$',category='success')
                
            else:
                flash(f'Your Budget is not enough to by {p_item_obj.name}',category='danger')
        sold_item = request.form.get('sold_item')
        s_item_obj = Item.query.filter_by(name=sold_item).first()
        if s_item_obj:
            if current_user.can_sell(s_item_obj):
                s_item_obj.sell(current_user)
                flash(f'success,you have sold {s_item_obj.name} for {s_item_obj.price}$',category='success')
    
        return redirect(url_for('Market'))     

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html',items=items,purchaseFrom=purchaseItemForm,owned_items=owned_items,sellItemForm=sellItemForm)
    

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
        login_user(user)
        flash(f'Acount Created Successfully, you are now logged in as {user.username}',category='success')
        
        return redirect(url_for('Market'))
    
    if form.errors:
        for err_msgs in form.errors.values():
            for err_msg in err_msgs:
                flash(f'{err_msg}', 'danger')
    
    return render_template('register.html', form=form)
