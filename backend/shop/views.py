import os

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename, safe_join
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.shop.models import Category, Product
from backend.accounts.models import User
from backend.constants.http_response_codes import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from backend.db import db


shop = Blueprint('shop', __name__, url_prefix='/shop')

ALLOWED_EXTENSIONS = ('jpg', 'png', 'jpeg')


def allowed_image(filename):
    """Validate images extensions"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@shop.post('/upload_product')
@jwt_required()
def upload_product():
    """Process POST request and create product."""
    # Get owner id
    current_user = get_jwt_identity()
    # Get data of product
    category: str = request.form.get('category')
    name: str = request.form.get('name')
    image = request.files.get('image')
    description: str = request.form.get('description')
    price: float = request.form.get('price')
    # Validate data of product
    if Category.query.filter_by(name=category).first() is None:
        return jsonify({'error': 'No such category'}), HTTP_400_BAD_REQUEST
    # Check if price is numeric and can be float
    try:
        float(price)
    except ValueError:
        return jsonify({'error': 'Price must be numeric'}), HTTP_400_BAD_REQUEST
    # Check if image was uploaded
    if image is not None:
        # Validate image
        if not allowed_image(image.filename):
            return jsonify({'error': 'An image should be .png, .jpeg or .jpg'}), HTTP_400_BAD_REQUEST
        # Create media dir if doesn't exist
        os.makedirs(os.environ.get('UPLOAD_FOLDER') + 'products/', exist_ok=True)
        # Create secure filename, path to file and save it
        image_name: str = secure_filename(image.filename)
        image_path: str = safe_join(os.environ.get('UPLOAD_FOLDER') + 'products', image_name)
        image.save(image_path)
    else:
        # Save None if no image was given
        image_path = None
    # Save product
    product = Product(category=Category.query.filter_by(name=category).first().id,
                      owner=current_user,
                      name=name,
                      image=image_path,
                      description=description,
                      price=price)

    db.session.add(product)
    db.session.commit()
    return jsonify({"message": 'Product uploaded', 'Product': name}), HTTP_201_CREATED


@shop.get('/products')
def get_products():
    """Process GET request and return product list"""
    # Get products from db
    products: list = Product.query.all()
    products_list = []
    for product in products:
        # Save product data in the list
        products_list.append({
            'id': product.id,
            'category': Category.query.filter_by(id=product.category_id).first().name,
            'owner': User.query.filter_by(id=product.owner_id).first().email,
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
    if not current_user == product.owner:
        return jsonify({'error': 'Only owner can delete the product.'})

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
    if not current_user == product.owner:
        return jsonify({'error': 'Only owner can change the product'})
    # Get data if was given else get old data
    category = request.json.get('category', product.category)
    name = request.json.get('name', product.category)
    description = request.json.get('description', product.description)
    price = request.json.get('price', product.price)
    # Validate new data
    if Category.query.filter_by(name=category).first() is None:
        return jsonify({'error': 'No such category'}), HTTP_400_BAD_REQUEST
    if not price.isalnum():
        return jsonify({'error': 'Price must be numeric'}), HTTP_400_BAD_REQUEST
    # Save data
    product.category = category
    product.name = name
    product.description = description
    product.price = price

    db.session.commit()
    return jsonify({
        'id': product.id,
        'category': product.category,
        'name': product.name,
        'description': product.description,
        'price': product.price,
    })
