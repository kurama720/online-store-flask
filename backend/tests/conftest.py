import pytest
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from backend.app import create_app
from backend.config import TestingConfig
from backend.db import db
from backend.accounts.models import User
from backend.shop.models import Product


@pytest.fixture(scope="session")
def app(request):
    """Create app with test config"""
    app = create_app(TestingConfig)
    return app


@pytest.fixture(scope='session')
def create_test_db(app):
    """Create testing database if it doesn't exist"""
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
    yield engine.url
    drop_database(engine.url)


@pytest.fixture(scope='function')
def fake_db(app, create_test_db):
    """Create tables in db. Drop database and delete it after testing."""
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def create_user():
    """Create testing user. Return user and his credentials"""
    email = 'test@test.com'
    pwd = 'Test1234'
    hash_pwd = generate_password_hash(pwd)
    user = User(email=email, password=hash_pwd)
    db.session.add(user)
    db.session.commit()
    return user, email, pwd


@pytest.fixture(scope='function')
def create_token(create_user):
    """Create token for authentication"""
    user, *credentials = create_user
    access_token = create_access_token(identity=user.id)
    return access_token


@pytest.fixture(scope='function')
def create_product(create_token):
    """Create testing product in db"""
    owner = User.query.filter_by(email='test@test.com').first()
    product = Product(name='test product', description='test tasty product', price=2.49, owner_id=owner.id)
    db.session.add(product)
    db.session.commit()
    return product

