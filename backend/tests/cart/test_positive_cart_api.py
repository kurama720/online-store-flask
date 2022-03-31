from flask import session


class TestCartPositive:
    """Test positive cart api scenarios"""

    def test_cart_add(self, client, product):
        """Test positive cart add product scenario"""
        # GIVEN product data (quantity, override param) and product id
        # WHEN creating cart and adding product to the cart
        # THEN return status code 201 and 'Product was added into cart successfully' msg
        with client:
            cart_data = {'quantity': 1, 'override': False}
            response = client.post(f'/cart/cart_add/{product.id}', json=cart_data)
            expected_msg = {'message': 'Product was added into cart successfully'}
            msg = response.json

            assert response.status_code == 201
            assert expected_msg == msg
            assert len(session['cart']) == 1
            assert session['cart'][str(product.id)]

    def test_cart_remove(self, client, product):
        """Test positive cart remove product scenario"""
        # GIVEN product id
        # WHEN removing product from cart
        # THEN return status code 200 and 'Product was removed from cart' msg
        with client:
            cart_data = {'quantity': 1, 'override': False}
            client.post(f'/cart/cart_add/{product.id}', json=cart_data)
            assert len(session['cart']) == 1

            response = client.delete(f'/cart/cart_remove/{product.id}')
            expected_msg = {'message': 'Product was removed from cart'}
            msg = response.json

            assert response.status_code == 200
            assert len(session['cart']) == 0
            assert expected_msg == msg

    def test_cart_detail(self, client, product):
        """Test positive cart detail scenario"""
        # WHEN GET request to the endpoint
        # THEN return status code 200 and data in cart
        with client:
            cart_data = {'quantity': 1, 'override': False}
            client.post(f'/cart/cart_add/{product.id}', json=cart_data)
            assert len(session['cart']) == 1

            response = client.get('/cart/cart_detail')

            assert response.status_code == 200
            assert len(response.json['User cart']) == 1

    def test_cart_clear(self, client, product):
        """Test positive cart clear scenario"""
        # WHEN POST request to the endpoint
        # THEN return status code 200 and remove cart from the session
        with client:
            cart_data = {'quantity': 1, 'override': False}
            client.post(f'/cart/cart_add/{product.id}', json=cart_data)
            assert len(session['cart']) == 1

            response = client.post('/cart/cart_clear')

            assert response.status_code == 200
            assert session.get('cart') is None
            assert len(session) == 0
