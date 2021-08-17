from flask import render_template,redirect,url_for
from flask.helpers import url_for
from  . import main
from .forms import RegisterForm,LoginForm
from ..models import User
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
#views
@main.route('/')
def index():
    '''
    view root page function that returns indext.html and its data
    '''
    return render_template('index.html')
@main.route('/login', methods=['GET', 'POST'])
def login():
    '''Instantiate login form'''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('main.index'))
        return '<h1> Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    return render_template('login.html',form=form)
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    '''Instantiate Sign Up form'''
    form = RegisterForm()
    if form.validate_on_submit():
         hashed_password = generate_password_hash(form.password.data,method='sha256')
         new_user =User(username=form.username.data, email=form.email.data,password=hashed_password)
         db.session.add(new_user)
         db.session.commit()
         
         return "<h1> New user has been added </h1>"
        # return '<h2>' + form.username.data + ' '+ form.email.data + ' ' + form.password.data + '</h2>'
    return render_template('signup.html',form=form)