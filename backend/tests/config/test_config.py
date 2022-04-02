import os

from backend.app import create_app
from backend.config import TestingConfig, DevelopmentConfig, ProductionConfig


class TestConfig:

    def test_create_testing_app(self):
        """Test create app with testing config"""
        # GIVEN testing config
        # WHEN app is created with testing config
        # THEN check app has proper settings
        app = create_app(TestingConfig)

        assert app.config.get('TESTING')
        assert app.config.get('DEBUG')
        assert app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')

    def test_create_dev_app(self):
        """Test create app with development config"""
        # GIVEN development config
        # WHEN app is created with development config
        # THEN check app has proper settings
        app = create_app(DevelopmentConfig)

        assert app.config.get('DEBUG')
        assert not app.config.get('TESTING')
        assert app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('SQLALCHEMY_DATABASE_URI')

    def test_create_prod_app(self):
        """Test create app with production config"""
        # GIVEN production config
        # WHEN app is created with production config
        # THEN check app has proper settings
        app = create_app(ProductionConfig)

        assert not app.config.get('DEBUG')
        assert not app.config.get('TESTING')
        assert app.config.get('SQLALCHEMY_DATABASE_URI') == os.environ.get('SQLALCHEMY_DATABASE_URI')
