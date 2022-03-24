"""Main module for app factory function"""

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from backend.db import db
from backend.config import DevelopmentConfig
from backend.accounts.views import auth
from backend.shop.views import shop


def create_app(test_config=None):
    """Project configuration"""
    app = Flask(__name__, instance_relative_config=True)
    # Get constants for configuration
    if test_config is None:
        app.config.from_object(DevelopmentConfig())
    else:
        app.config.from_mapping(test_config)
    # Initialize db
    db.app = app
    db.init_app(app)
    # Initialize migrations
    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True)
    # Make JWTManager
    JWTManager(app)
    # Register services
    app.register_blueprint(auth)
    app.register_blueprint(shop)

    return app
