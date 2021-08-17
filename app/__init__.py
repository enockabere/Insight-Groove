from flask import  Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(config_name):
    
    #initializing flask application
    app = Flask(__name__)

    #setup app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    #regitster blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app                   
