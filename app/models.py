from sqlalchemy.orm import backref
from . import db
from  flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(30), unique=True,nullable=False)
    password = db.Column(db.String(80))
    pitch = db.relationship('Pitch')
    liked = db.relationship('PostLike', foreign_keys='PostLike.users_id', backref='users',lazy='dynamic')
    
    def like_pitch(self,post):
        if not self.has_liked_post(post):
            like = PostLike(users_id=self.id,post_id=post.id)
            db.session.add(like)
    def unlike_post(self,post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(users_id=self.id,post_id=post.id).delete()
    def has_liked_post(self,post):
        return PostLike.query.filter_by(PostLike.users_id==self.id,PostLike.post_id==post.id).count()>0
    def __repr__(self):
        return f'User{self.username}'
class Pitch (db.Model):
    __tablename__= "pitchs"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    message = db.Column(db.String(), unique=True,nullable=False)
    category = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    likes = db.relationship('PostLike', backref='pitchs', lazy='dynamic')
    
class PostLike(db.Model):
    __tablename__= 'post_like'
    
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitchs.id') )
    like = db.Column(db.Integer,nullable=False)
    dislike = db.Column(db.Integer,nullable=False)
    
    