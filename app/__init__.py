from flask import  Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import *
from flask_login import LoginManager,login_manager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager= LoginManager()
def create_app(config_name):
    
    #initializing flask application
    app = Flask(__name__)

    #setup app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #regitster blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app                   
