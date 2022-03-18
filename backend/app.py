import os

from flask import Flask
from flask_jwt_extended import JWTManager


def create_app(test_config=None):
    """Project configuration"""
    app = Flask(__name__, instance_relative_config=True)
    # Get constants for configuration
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY'),
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),
        )
    else:
        app.config.from_mapping(test_config)

    JWTManager(app)

    return app
