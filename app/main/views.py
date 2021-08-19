from flask import render_template,redirect,url_for
from flask.helpers import url_for
import app
from  . import main
from .forms import RegisterForm,LoginForm,PitchForm
from ..models import User, Pitch
from app import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import current_user,login_user,logout_user,login_required

# creating an auth instance

login_manager.login_view = 'login'


#views
@main.route('/')
def index():
    '''
    view root page function that returns indext.html and its data
    '''
    return render_template('index.html')
@main.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Instantiate login form
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user,form.remember)
                return redirect(url_for('main.dashboard'))
        return '<h1> Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    return render_template('login.html',form=form)
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    Instantiate Sign Up form
    '''
    form = RegisterForm()
    if form.validate_on_submit():
         hashed_password = generate_password_hash(form.password.data,method='sha256')
         new_user =User(username=form.username.data, email=form.email.data,password=hashed_password)
         db.session.add(new_user)
         db.session.commit()
         return redirect(url_for('main.login'))
        # return '<h2>' + form.username.data + ' '+ form.email.data + ' ' + form.password.data + '</h2>'
    return render_template('signup.html',form=form)
@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    
    # fetch data
    pitch = Pitch.query.all()

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        message = form.message.data

        new_pitch = Pitch(category=category, message=message)

        # add data to db
        db.session.add(new_pitch)
        db.session.commit()
        print("Schedule created successfully")
        return '<h2>' + form.category.data +'</h2>'
    return render_template('dashboard.html',form=form,name=current_user.username, pitch=pitch)
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))