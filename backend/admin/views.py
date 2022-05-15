from flask import Blueprint, request, jsonify
import validators
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_refresh_token, create_access_token, jwt_required, get_jwt_identity

from backend.constants.http_response_codes import HTTP_400_BAD_REQUEST,\
                                                  HTTP_409_CONFLICT,\
                                                  HTTP_201_CREATED,\
                                                  HTTP_200_OK,\
                                                  HTTP_401_UNAUTHORIZED, \
                                                  HTTP_403_FORBIDDEN
from backend.db import db
from backend.shop.models import Category
from backend.accounts.models import User


admin_managing = Blueprint('admin_managing', __name__, url_prefix='/admin_managing')


@admin_managing.post('/create_admin')
def create_admin():
    """Process POST request and register an admin user"""
    # Get data
    email = request.json['email']
    password = request.json['password']
    # Validate data
    if len(password) < 8:
        return jsonify({'error': 'Password is too short'}), HTTP_400_BAD_REQUEST
    if not validators.email(email):
        return jsonify({'error': 'Email is not valid'}), HTTP_400_BAD_REQUEST
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': 'Email already exists'}), HTTP_409_CONFLICT
    # Hash password and save the admin user
    pwd_hash = generate_password_hash(password)
    admin_user = User(email=email, password=pwd_hash, is_staff=True)

    db.session.add(admin_user)
    db.session.commit()
    return jsonify({"message": 'Admin user created',
                    'user': {
                        'email': email
                    }}), HTTP_201_CREATED


@admin_managing.post('/login_admin')
def login_admin():
    """Process POST request and login an admin user, return tokens"""
    # Get credentials
    email = request.json.get('email', '')
    password = request.json.get('password', '')
    admin_user = User.query.filter_by(email=email).first_or_404()
    # Compare given password hash and password hash in database
    is_pwd_correct = check_password_hash(admin_user.password, password)
    if is_pwd_correct:
        # Create tokens and return them
        refresh = create_refresh_token(identity=admin_user.id)
        access = create_access_token(identity=admin_user.id)
        return jsonify({
            'refresh': refresh,
            'access': access,
            'user_email': admin_user.email
        }), HTTP_200_OK

    return jsonify({'error': 'Wrong credentials'}), HTTP_401_UNAUTHORIZED


@admin_managing.post('/create_category')
def create_category():
    """Process POST request and create category."""
    name = request.json.get('name')
    if Category.query.filter_by(name=name).first() is not None:
        return jsonify({'message': f'Category: {name} already exists'}), HTTP_409_CONFLICT

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': f'Category: {name} was created'}), HTTP_201_CREATED
