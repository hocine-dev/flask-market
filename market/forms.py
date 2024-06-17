from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='User Name:')
    email= StringField(label='Email Adresse:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirme Password:')
    submit=SubmitField(label='Create Account')