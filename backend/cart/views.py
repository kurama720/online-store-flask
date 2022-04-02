from flask import session, Blueprint, request, jsonify

from backend.constants.http_response_codes import HTTP_201_CREATED,\
                                                  HTTP_200_OK,\
                                                  HTTP_400_BAD_REQUEST,\
                                                  HTTP_404_NOT_FOUND
from backend.shop.models import Product
from backend.cart.cart import Cart


cart = Blueprint('cart', __name__, url_prefix='/cart')


@cart.post('/cart_add/<int:product_id>')
def cart_add(product_id):
    """
    Process POST request and add a product to the cart or add quantity to the already existing one.
    :param product_id: int
    """
    cart = Cart(session)
    product = Product.query.filter_by(id=product_id).first_or_404()
    quantity = request.json.get('quantity', 1)
    override = request.json.get('override', False)
    if quantity <= 0:
        return jsonify({'message': 'Product quantity must be positive integer.'}), HTTP_400_BAD_REQUEST
    if not isinstance(override, bool):
        return jsonify({'message': 'Override param must be the logic type object.'}), HTTP_400_BAD_REQUEST
    cart.add(product=product, quantity=quantity, override_quantity=override)
    return jsonify({'message': 'Product was added into cart successfully'}), HTTP_201_CREATED


@cart.delete('/cart_remove/<int:product_id>')
def cart_remove(product_id):
    """
    Process POST request and remove product from the cart.
    :param product_id:  int
    """
    cart = Cart(session)
    product = Product.query.filter_by(id=product_id).first_or_404()
    # Check if product is in the cart
    if not session['cart'].get(str(product.id)):
        return jsonify({'message': 'Product is not in the cart'}), HTTP_404_NOT_FOUND
    cart.remove(product)
    return jsonify({'message': 'Product was removed from cart'}), HTTP_200_OK


@cart.get('/cart_detail')
def cart_detail():
    """
    Process GET request and return the cart and total cost of it.
    """
    cart = Cart(session)
    return jsonify({'Total price': float(cart.get_total_price()), 'User cart': cart.cart}), HTTP_200_OK


@cart.post('/cart_clear')
def cart_clear():
    """
    Process POST request and clear the cart.
    """
    cart = Cart(session)
    cart.clear()
    return jsonify({'message': 'Cart was cleared'}), HTTP_200_OK
