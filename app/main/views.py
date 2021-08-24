from flask import render_template,redirect,url_for,request,jsonify
from flask.helpers import flash, url_for
from flask.templating import render_template_string
from flask_wtf import form
from wtforms.validators import data_required
import app
from  . import main
from .forms import RegisterForm,LoginForm,BlogForm,CommentForm
from ..models import Blog, User, Blog,Comment
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
    likes = Comment.query.all()
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data,users_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    blog = Blog.query.all()
    return render_template('dashboard.html',likes=likes, form=form,blog=blog)
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
                return redirect(url_for('main.profile'))
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
    blog = Blog.query.all()

    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        message = form.message.data

        new_blog = Blog(title=title, message=message,user_id=current_user.id)

        # add data to db
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.profile'))
    return render_template('profile.html',form=form,name=current_user.username, blog=blog)
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
@main.route('/delete-blog', methods=['POST'])
def delete_blog():
    blog = json.loads(request.data)
    blogId = blog['blogId']
    blog = Blog.query.get(blogId)
    if blog:
        if blog.user_id == current_user.id:
            db.session.delete(blog)
            db.session.commit()
    return jsonify({})
@main.route('/fullblog', methods=['GET', 'POST'])
def fullblog():
    
    return render_template('full.html')
