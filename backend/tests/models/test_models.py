from werkzeug.security import generate_password_hash, check_password_hash

from backend.accounts.models import User
from backend.shop.models import Product, Category


class TestModels:
    """Testing models class"""

    def test_create_user(self):
        """Test creating user"""
        # GIVEN user data
        # WHEN user is saved
        # THEN check user has proper data
        email = 'test@test.com'
        pwd = 'Test1234'
        pwd_hash = generate_password_hash(pwd)
        user = User(email=email, password=pwd_hash)

        assert user.email == email
        assert check_password_hash(user.password, pwd)

    def test_create_product(self):
        """Test creating product"""
        # GIVEN product data
        # WHEN product is saved
        # THEN check product has proper data
        name = 'test product'
        description = 'tasty product'
        price = 2.49
        product = Product(name=name, description=description, price=price)

        assert product.name == name
        assert product.description == description
        assert product.price == price

    def test_create_category(self):
        """Test creating category"""
        # GIVEN category data
        # WHEN category is saved
        # THEN check category has proper data
        name = 'Test category'
        category = Category(name=name)

        assert category.name == name
