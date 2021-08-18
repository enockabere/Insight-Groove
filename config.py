import  os
import secrets
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= secrets.token_hex(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI=''


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI=''
    
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}