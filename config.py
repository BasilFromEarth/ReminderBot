import os


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
