import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from backend.db import db
from backend.config import DevelopmentConfig
from backend.accounts.auth import auth
from backend.accounts import models


def create_app(test_config=None):
    """Project configuration"""
    app = Flask(__name__, instance_relative_config=True)
    # Get constants for configuration
    if test_config is None:
        app.config.from_object(DevelopmentConfig())
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True)

    JWTManager(app)

    app.register_blueprint(auth)

    return app
