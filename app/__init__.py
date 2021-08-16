from flask import  Flask

#initializing flask application
app = Flask(__name__)

from app import  views,error