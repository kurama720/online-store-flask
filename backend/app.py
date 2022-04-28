"""Main module for app factory function"""
import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

from backend.db import db
from backend.config import DevelopmentConfig
from backend.accounts.views import auth
from backend.shop.views import shop
from backend.admin.admin import admin
from backend.admin.views import admin_managing
from backend.cart.views import cart


def create_app(test_config=None):
    """Project configuration"""
    app = Flask(__name__, instance_relative_config=True)
    # Get constants for configuration
    if test_config is None:
        app.config.from_object(DevelopmentConfig())
    else:
        app.config.from_object(test_config)
    # Initialize db
    db.app = app
    db.init_app(app)
    # Initialize migrations
    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True, directory=os.environ.get('MIGRATIONS_DIR'))
    # Make JWTManager
    JWTManager(app)
    # Initialize admin
    admin.init_app(app)
    CORS(app, resources={r"/*": {"origins": r"http://localhost:3000/*"}})
    # Register services
    app.register_blueprint(auth)
    app.register_blueprint(shop)
    app.register_blueprint(admin_managing)
    app.register_blueprint(cart)

    return app
