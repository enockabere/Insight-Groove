from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length

class LoginForm(FlaskForm):
   username = StringField('username', validators=[InputRequired(),Length(min=4,max=20)])
   password = PasswordField('password', validators=[InputRequired(),Length(min=6,max=20)])
   remember = BooleanField('remember me')
   
class  RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=4,max=20)])
    email = StringField('email', validators=[Email(message='Invalid email'),Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=6,max=20)])