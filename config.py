'''Config'''

class Config(object):
    '''
    Basic Configuration
    '''


class DevelopmentConfig(Config):
    '''
    Development Configutarions
    '''

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    '''
    Production Configurations
    '''

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

