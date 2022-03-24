from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import validators
from flask_jwt_extended import create_refresh_token, create_access_token, jwt_required, get_jwt_identity

from backend.constants.http_response_codes import HTTP_400_BAD_REQUEST, \
                                                  HTTP_201_CREATED, \
                                                  HTTP_409_CONFLICT, \
                                                  HTTP_200_OK, \
                                                  HTTP_401_UNAUTHORIZED
from backend.db import db
from backend.accounts.models import User

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.post('/register')
def register():
    """Process POST request and register a user"""
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
    # Hash password and save user
    pwd_hash = generate_password_hash(password)
    user = User(email=email, password=pwd_hash)

    db.session.add(user)
    db.session.commit()
    return jsonify({"message": 'User created',
                    'user': {
                        'email': email
                    }}), HTTP_201_CREATED


@auth.post('/login')
def login():
    """Process POST request and login a user, return tokens"""
    # Get credentials
    email = request.json.get('email', '')
    password = request.json.get('password', '')
    user = User.query.filter_by(email=email).first_or_404()
    # Compare given password hash and password hash in database
    is_pwd_correct = check_password_hash(user.password, password)
    if is_pwd_correct:
        # Create tokens and return them
        refresh = create_refresh_token(identity=user.id)
        access = create_access_token(identity=user.id)
        return jsonify({
            'refresh': refresh,
            'access': access,
            'user_email': user.email
        }), HTTP_200_OK

    return jsonify({'error': 'Wrong credentials'}), HTTP_401_UNAUTHORIZED


@auth.get('info')
@jwt_required()
def account_info():
    """Process GET request and return user's info"""
    # Get user by token
    current_user = User.query.filter_by(id=get_jwt_identity()).first_or_404()
    return jsonify({
        "user": {
            'email': current_user.email,
            'products': [product.id for product in current_user.products]
        }})
