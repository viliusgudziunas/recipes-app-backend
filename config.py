import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True,
    DEVELOPMENT = True


config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
