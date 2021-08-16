from flask import  Flask
from flask_bootstrap import Bootstrap

#initializing flask application
app = Flask(__name__)
app.config['SECRET_KEY']= 'Thisissupposedtobesecret'

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
                      
from app import  views,error