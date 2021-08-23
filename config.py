import  os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

class ProdConfig(Config):
    
    DEBUG = True

class DevConfig(Config):
        
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
