from flask_jwt_extended import create_access_token

from backend.accounts.models import User


class TestShopNegative:
    """Test negative shop api scenarios"""

    def test_upload_product_invalid_category(self, client, token_user):
        """Test negative product upload scenario"""
        # GIVEN product data with invalid category
        # WHEN saving product in db
        # THEN return status code 400 and 'No such category' msg
        product_data = {'category': 'Tea', 'name': 'product', 'description': 'test product', 'price': 2.49}
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        response = client.post('/shop/upload_product', json=product_data, headers=headers)
        expected_msg = {'error': 'No such category'}
        msg = response.json

        assert response.status_code == 400
        assert expected_msg == msg

    def test_upload_product_invalid_price(self, client, token_user):
        """Test negative product upload scenario"""
        # GIVEN product data with invalid price
        # WHEN saving product in db
        # THEN return status code 400 and 'Price must be numeric' msg
        product_data = {'name': 'product', 'description': 'test product', 'price': 'Two dollars and forty nine cents'}
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        response = client.post('/shop/upload_product', json=product_data, headers=headers)
        expected_msg = {'error': 'Price must be numeric'}
        msg = response.json

        assert response.status_code == 400
        assert expected_msg == msg

    def test_delete_nonexistent_product(self, client, token_user):
        """Test negative delete product scenario"""
        # GIVEN nonexistent product id
        # WHEN deleting product from db
        # THEN return status code 404
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        nonexistent_id = 2222
        response = client.delete(f'/shop/delete_product/{nonexistent_id}', headers=headers)

        assert response.status_code == 404

    def test_delete_product_not_by_an_owner(self, client, product):
        """Test negative delete product scenario"""
        # GIVEN product id and token of not a product owner
        # WHEN deleting product
        # THEN return status code 400 and 'Only owner can delete the product' msg
        user = User(email='tester@test.com', password='Test1234')
        token = create_access_token(identity=user.id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = client.delete(f'/shop/delete_product/{product.id}', headers=headers)
        expected_msg = {'error': 'Only owner can delete the product.'}
        msg = response.json

        assert response.status_code == 400
        assert expected_msg == msg

    def test_update_product_not_by_an_owner(self, client, product):
        """Test negative update product scenario"""
        # GIVEN product id and token of not a product owner
        # WHEN updating product
        # THEN return status code 400 and 'Only owner can change the product' msg
        user = User(email='tester@test.com', password='Test1234')
        token = create_access_token(identity=user.id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data_to_update = {'price': 2000}
        response = client.patch(f'/shop/update_product/{product.id}',
                                json=data_to_update, headers=headers)
        expected_msg = {'error': 'Only owner can change the product'}
        msg = response.json

        assert response.status_code == 400
        assert expected_msg == msg

    def test_update_product_with_invalid_price(self, client, token_user, product):
        """Test negative update product scenario"""
        # GIVEN product id and invalid price
        # WHEN updating product
        # THEN return status code 400 and 'Price must be number' msg
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        data_to_update = {'price': 'wrong price'}
        response = client.patch(f'/shop/update_product/{product.id}',
                                json=data_to_update, headers=headers)
        expected_msg = {'error': 'Price must be numeric'}
        msg = response.json

        assert response.status_code == 400
        assert expected_msg == msg

    def test_update_with_invalid_category(self, client, token_user, product):
        """Test negative update product scenario"""
        # GIVEN product id and invalid category
        # WHEN updating product
        # THEN return status code 400 and 'No such category' msg
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        data_to_update = {'category': 'Nonexistent category'}
        response = client.patch(f'/shop/update_product/{product.id}',
                                json=data_to_update, headers=headers)
        expected_msg = {'error': 'No such category'}
        msg = response.json

        assert response.status_code == 400
        assert expected_msg == msg

    def test_get_product_by_id(self, client):
        """Test negative get product by id scenario"""
        # GIVEN nonexistent product id
        # WHEN getting product from db
        # THEN return status code 404
        nonexistent_id = 2222
        response = client.get(f'/shop/products/{nonexistent_id}')

        assert response.status_code == 404
