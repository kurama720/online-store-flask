import pytest
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from backend.app import create_app
from backend.config import TestingConfig
from backend.db import db
from backend.accounts.models import User
from backend.shop.models import Product, Category
from backend.admin.models import AdminUser


@pytest.fixture(scope="session", autouse=True)
def app():
    """Create app with test config"""
    app = create_app(TestingConfig)
    app.app_context().push()
    return app


@pytest.fixture(scope='session', autouse=True)
def create_test_db(app):
    """Create testing database if it doesn't exist"""
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
    yield engine.url
    drop_database(engine.url)


@pytest.fixture(scope='function', autouse=True)
def fake_db(app):
    """Create tables in db. Drop database and delete it after testing."""
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def client(app):
    return app.test_client()


@pytest.fixture(scope='function')
def user():
    """Create testing user. Return user and his credentials"""
    email = 'test@test.com'
    pwd = 'Test1234'
    hash_pwd = generate_password_hash(pwd)
    user = User(email=email, password=hash_pwd)
    db.session.add(user)
    db.session.commit()
    return user, email, pwd


@pytest.fixture(scope='function')
def token_user(user):
    """Create token for authentication"""
    user, *credentials = user
    access_token = create_access_token(identity=user.id)
    return access_token


@pytest.fixture(scope='function')
def product(token_user):
    """Create testing product in db"""
    owner = User.query.filter_by(email='test@test.com').first()
    product = Product(name='test product', description='test tasty product', price=2.49, owner_id=owner.id)
    db.session.add(product)
    db.session.commit()
    return product


@pytest.fixture(scope='function')
def admin():
    email = 'admin@admin.com'
    pwd = 'Test1234'
    hash_pwd = generate_password_hash(pwd)
    admin = AdminUser(email=email, password=hash_pwd)
    db.session.add(admin)
    db.session.commit()
    return admin, email, pwd


@pytest.fixture(scope='function')
def token_admin(admin):
    """Create token for admin"""
    user, *credentials = admin
    access_token = create_access_token(identity=user.id)
    return access_token


@pytest.fixture(scope='function')
def category():
    category = Category(name='Test')
    db.session.add(category)
    db.session.commit()
    return category
