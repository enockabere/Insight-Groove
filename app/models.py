from . import db
# from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(30), unique=True,nullable=False)
    password = db.Column(db.String(80))
    
    # @property
    # def password(self):
    #     raise AttributeError('You can not read the password attribute')
    # @password.setter
    # def password(self, password):
    #     self.password = generate_password_hash(password)
    # def verify_password(self, password):
    #     return check_password_hash(self.password, password)
    def __repr__(self):
        return f'User{self.username}'
