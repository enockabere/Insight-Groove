from flask import render_template,redirect,url_for,request,jsonify
from flask.helpers import flash, url_for
from flask_wtf import form
from wtforms.validators import data_required
import app
from  . import main
from .forms import RegisterForm,LoginForm,PitchForm,CommentForm
from ..models import User, Pitch,PostLike
from app import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import current_user,login_user,logout_user,login_required
import json

# creating an auth instance
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

login_manager.login_view = 'main.login'


#views
@main.route('/', methods=['GET', 'POST'])
def dashboard():
    likes = PostLike.query.all()
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = PostLike(comment=form.comment.data,users_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    pitch = Pitch.query.all()
    return render_template('dashboard.html',likes=likes, form=form,pitch=pitch)
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
                login_user(user,remember=True)
                return redirect(url_for('main.dashboard'))
        return '<h1> Invalid username or password</h1>'
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
@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    
    # fetch data
    pitch = Pitch.query.all()

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        message = form.message.data

        new_pitch = Pitch(category=category, message=message,user_id=current_user.id)

        # add data to db
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.profile'))
    return render_template('profile.html',form=form,name=current_user.username, pitch=pitch)
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
@main.route('/delete-pitch', methods=['POSt'])
def delete_pitch():
    pitch = json.loads(request.data)
    pitchId = pitch['pitchId']
    pitch = Pitch.query.get(pitchId)
    if pitch:
        if pitch.user_id == current_user.id:
            db.session.delete(pitch)
            db.session.commit()
    return jsonify({})
