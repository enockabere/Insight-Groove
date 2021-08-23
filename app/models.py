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

    def __repr__(self):
        return f'User{self.username}'
class Pitch (db.Model):
    __tablename__= "pitchs"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String(100), unique=True,nullable=False)
    message = db.Column(db.String(), unique=True,nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    likes = db.relationship('PostLike', backref='pitchs', lazy='dynamic')
    
class PostLike(db.Model):
    __tablename__= 'post_like'
    
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitchs.id') )
    comment = db.Column(db.String(), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)

    
    