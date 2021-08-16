from flask import render_template
from app import  app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length

class LoginForm(FlaskForm):
   username = StringField('username', validators=[InputRequired(),Length(min=4,max=20)])
   password = PasswordField('password', validators=[InputRequired(),Length(min=6,max=20)])
   remember = BooleanField('remember me')

#views
@app.route('/')
def index():
    '''
    view root page function that returns indext.html and its data
    '''
    return render_template('index.html')
@app.route('/login')
def login():
    '''Instantiate login form'''
    form = LoginForm()
    
    return render_template('login.html',form=form)
@app.route('/signup')
def signup():
    return render_template('signup.html')