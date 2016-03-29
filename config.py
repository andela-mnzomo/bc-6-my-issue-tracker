# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    ''' Common configurations '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    '''Config for development '''
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    # Define database configurations
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'data-dev.sqlite')
        
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

class ProductionConfig(Config):
    ''' Config for production '''
    PORT = int(os.environ.get("PORT", 5000))
    HOST = '0.0.0.0'
    
    # Define database configurations
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'data-dev.sqlite')
        
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

