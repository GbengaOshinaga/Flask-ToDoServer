from os import getenv

class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI',
        default='postgresql://localhost/todo_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}