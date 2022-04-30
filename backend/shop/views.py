from decimal import Decimal

from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import desc
from sqlalchemy.exc import DataError

from backend.shop.models import Category, Product
from backend.accounts.models import User
from backend.constants.http_response_codes import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from backend.db import db
from backend.services.connect_aws import s3, BUCKET_NAME


shop = Blueprint('shop', __name__, url_prefix='/shop')

ALLOWED_EXTENSIONS = ('jpg', 'png', 'jpeg')


def allowed_image(filename):
    """Validate images extensions"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@shop.post('/upload_product')
@jwt_required()
def upload_product():
    """Process POST request and create product."""
    try:
        # Get owner id
        current_user = User.query.filter_by(id=get_jwt_identity()).first_or_404()
        # Get data of product
        category: str = request.form.get('category', None)
        name: str = request.form.get('name')
        image = request.files.get('image')
        description: str = request.form.get('description')
        price: (float, int) = request.form.get('price')
        # Validate data of product
        if category is not None:
            if Category.query.filter_by(name=category).first() is None:
                return jsonify({'error': 'No such category'}), HTTP_400_BAD_REQUEST
        # Check if image was uploaded
        if image is not None:
            filename = secure_filename(image.filename)
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=filename,
                Body=image,
                Tagging='public=yes',
                ContentType='image/png'
            )
        else:
            filename = None
        # Save product
        product = Product(category=Category.query.filter_by(name=category).first(),
                          owner=current_user,
                          name=name,
                          image=filename,
                          description=description,
                          price=float(price))

        db.session.add(product)
        db.session.commit()
        return jsonify({"message": 'Product uploaded', 'Product': name}), HTTP_201_CREATED
    except (DataError, ValueError):
        return jsonify({'error': 'Price must be numeric'}), HTTP_400_BAD_REQUEST


@shop.get('/products')
def get_products():
    """Process GET request and return product list"""
    # Get products from db
    products: list = Product.query.order_by(desc(Product.created)).all()
    products_list = []
    for product in products:
        # Save product data in the list
        if product.available:
            category = Category.query.filter_by(id=product.category_id).first()
            owner = User.query.filter_by(id=product.owner_id).first()
            products_list.append({
                'id': product.id,
                'category': category.name if category is not None else 'Other',
                'owner': owner.email if owner is not None else "Owner's account was deleted",
                'name': product.name,
                'image': product.image,
                'description': product.description,
                'price': float(product.price),
                'created': product.created,
                'updated': product.updated
            })
    return jsonify({'products': products_list}), HTTP_200_OK


@shop.delete('/delete_product/<int:product_id>')
@jwt_required()
def delete_product(product_id):
    """Process DELETE request and delete a product if the owner makes the request"""
    # Get user id from token
    current_user: int = get_jwt_identity()
    # Get product by id
    product = Product.query.filter_by(id=product_id).first_or_404()
    # Check if user is owner
    if not current_user == product.owner_id:
        return jsonify({'error': 'Only owner can delete the product.'}), HTTP_400_BAD_REQUEST

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product was deleted'}), HTTP_200_OK


@shop.patch('/update_product/<int:product_id>')
@shop.put('/update_product/<int:product_id>')
@jwt_required()
def update_product(product_id):
    """Process PATCH and PUT requests and update a product data"""
    # Get user id by token
    current_user: int = get_jwt_identity()
    # Get product by id
    product = Product.query.filter_by(id=product_id).first_or_404()
    # Check if user is owner
    if not current_user == product.owner_id:
        return jsonify({'error': 'Only owner can change the product'}), HTTP_400_BAD_REQUEST
    # Get data if was given else get old data
    category_name = request.json.get('category', None)
    name = request.json.get('name', product.name)
    description = request.json.get('description', product.description)
    price = request.json.get('price', product.price)
    # Validate new data
    # Check if category exists
    if category_name is not None:
        category = Category.query.filter_by(name=category_name).first()
        if category is None:
            return jsonify({'error': 'No such category'}), HTTP_400_BAD_REQUEST
        product.category = category
    if not isinstance(price, (float, int, Decimal)):
        return jsonify({'error': 'Price must be numeric'}), HTTP_400_BAD_REQUEST
    # Save data
    product.name = name
    product.description = description
    product.price = price

    db.session.commit()
    products_category = Category.query.filter_by(id=product.category_id).first()
    return jsonify({
        'id': product.id,
        'category': products_category.name if products_category is not None else "Other",
        'name': product.name,
        'description': product.description,
        'price': float(product.price),
    })


@shop.get('/products/<int:product_id>')
def get_product_by_id(product_id):
    """Process GET request and return product by id"""
    # Get product by id or 404
    product = Product.query.filter_by(id=product_id).first_or_404()
    # Get product's category
    category = Category.query.filter_by(id=product.category_id).first()
    owner = User.query.filter_by(id=product.owner_id).first()
    return jsonify({
        'id': product.id,
        'category': category.name if category is not None else 'Other',
        'owner': owner.email if owner is not None else "Owner's account was deleted",
        'name': product.name,
        'image': product.image,
        'description': product.description,
        'price': float(product.price),
        'created': product.created,
        'updated': product.updated
    }), HTTP_200_OK


@shop.get('/categories')
def get_categories():
    """Process GET request and return categories list"""
    # Get categories from db
    categories: list = Category.query.all()
    categories_list = []
    for category in categories:
        # Save category data in the list
        categories_list.append({
            'id': category.id,
            "category": category.name
            })
    return jsonify({'categories': categories_list}), HTTP_200_OK


@shop.get('/image/<path>')
def get_image(path):
    # product = Product.query.filter_by(id=4).first()
    # print(path)
    return send_file(path, mimetype='image/png')
