import os


class Config:
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


class DevelopmentConfig(Config):
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
