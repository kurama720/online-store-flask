"""Module for app config"""

import os


class Config:
    """Base config"""
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST')


class DevelopmentConfig(Config):
    """Config for development"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class TestingConfig(Config):
    """Config for testing"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
