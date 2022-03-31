from flask import session


class TestCartNegative:
    """Test negative cart api scenarios"""

    def test_cart_add_nonexistent_product(self, client):
        """Test negative cart add product scenario"""
        # GIVEN nonexistent product id
        # WHEN creating cart and adding product to the cart
        # THEN return status code 404
        with client:
            cart_data = {'quantity': 1}
            nonexistent_id = 12345
            response = client.post(f'/cart/cart_add/{nonexistent_id}', json=cart_data)

            assert response.status_code == 404
            assert len(session['cart']) == 0

    def test_cart_add_invalid_quantity(self, client, product):
        """Test negative cart add product scenario"""
        # GIVEN invalid quantity
        # WHEN creating cart and adding product to the cart
        # THEN return status code 404 and 'Product quantity must be positive integer.' msg
        with client:
            cart_data = {'quantity': -2}
            response = client.post(f'/cart/cart_add/{product.id}', json=cart_data)
            expected_msg = {'message': 'Product quantity must be positive integer.'}
            msg = response.json

            assert response.status_code == 400
            assert expected_msg == msg
            assert len(session['cart']) == 0

    def test_cart_add_invalid_override_param(self, client, product):
        """Test negative cart add product scenario"""
        # GIVEN invalid override param
        # WHEN creating cart and adding product to the cart
        # THEN return status code 404 and 'Override param must be the logic type object.' msg
        with client:
            cart_data = {'quantity': 1, 'override': 'true'}
            response = client.post(f'/cart/cart_add/{product.id}', json=cart_data)
            expected_msg = {'message': 'Override param must be the logic type object.'}
            msg = response.json

            assert response.status_code == 400
            assert expected_msg == msg
            assert len(session['cart']) == 0

    def test_cart_remove_nonexistent_product(self, client):
        """Test negative cart remove product scenario"""
        # GIVEN nonexistent product id
        # WHEN removing product from the cart
        # THEN return status code 404
        with client:
            nonexistent_id = 12345
            response = client.delete(f'/cart/cart_remove/{nonexistent_id}')

            assert response.status_code == 404

    def test_cart_remove_product_that_is_not_in_cart(self, client, product):
        """Test negative cart remove product scenario"""
        # GIVEN product id that is not in the cart
        # WHEN removing product from the cart
        # THEN return status code 404 and 'Product is not in the cart' msg
        with client:
            response = client.delete(f'/cart/cart_remove/{product.id}')
            expected_msg = {'message': 'Product is not in the cart'}
            msg = response.json

            assert response.status_code == 404
            assert expected_msg == msg

