"""Module for app config"""

import os


class Config:
    """Base config"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class DevelopmentConfig(Config):
    """Config for development"""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Config for testing"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')


class ProductionConfig(Config):
    """Config for production"""
    DEBUG = False
    TESTING = False
