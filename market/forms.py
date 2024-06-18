from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='User Name:',validators=[Length(min=4,max=30),DataRequired()])
    email= StringField(label='Email Adresse:',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6,max=30),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1',message='Password and confirm password mismatch.'),DataRequired()])
    submit=SubmitField(label='Create Account')