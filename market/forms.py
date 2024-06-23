from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if(user):
            raise ValidationError('Username already exist, please try another username')
    def validate_email(self,email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if(user):
            raise ValidationError('Email already exist, please try another username')   
        
    username = StringField(label='User Name:',validators=[Length(min=4,max=30),DataRequired()])
    email= StringField(label='Email Adresse:',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6,max=30),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1',message='Password and confirm password mismatch.'),DataRequired()])
    submit=SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):    
    username = StringField(label='User Name:',validators=[Length(min=4,max=30),DataRequired()])
    password = PasswordField(label='Password:',validators=[Length(min=6,max=30),DataRequired()])
    submit=SubmitField(label='Login')
    
class PurchaseItemForm(FlaskForm):
    submit=SubmitField(label='Purchase Item')
    
class SellItemForm(FlaskForm):
    submit=SubmitField(label='Sell Item')