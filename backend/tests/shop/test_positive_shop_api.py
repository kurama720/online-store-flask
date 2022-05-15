class TestShopPositive:
    """Test positive shop api scenarios"""

    def test_upload_product(self, client, token_user):
        """Test positive product upload scenario"""
        # GIVEN product data
        # WHEN save product in db
        # THEN return status code 201 and product's name
        product_data = {'name': 'product', 'description': 'test product', 'price': 2.49}
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        response = client.post('/shop/upload_product', data=product_data, headers=headers)
        expected_msg = {'Product': 'product', 'message': 'Product uploaded'}
        msg = response.json

        assert response.status_code == 201
        assert expected_msg == msg

    def test_get_product_list(self, client, product):
        """Test positive product list scenario"""
        # WHEN GET request to the endpoint
        # THEN return status code 200 and a list with one product
        response = client.get('/shop/products')
        expected_msg = 'test product'
        msg = response.json.get('products')[0]['name']

        assert response.status_code == 200
        assert len(response.json) == 1
        assert expected_msg == msg

    def test_delete_product(self, client, token_user, product):
        """Test positive product delete scenario"""
        # GIVEN product id
        # WHEN deleting product from bd
        # THEN return status code 200 and 'Product was deleted' msg
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        response = client.delete(f'/shop/delete_product/{product.id}', headers=headers)
        expected_msg = 'Product was deleted'
        msg = response.json.get('message')

        assert response.status_code == 200
        assert expected_msg == msg

    def test_update_product(self, client, token_user, product):
        """Test positive product update scenario"""
        # GIVEN product id and data to update
        # WHEN updating data of the product
        # THEN return status code 200 and product new data json
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        data_to_update = {'name': 'not a testing product', 'description': 'not a tasty product', 'price': 0}
        response = client.put(f'/shop/update_product/{product.id}',
                              data=data_to_update, headers=headers)
        expected_msg = {'category': 'Other', 'description': 'not a tasty product',
                        'price': 0, 'name': 'not a testing product', 'id': product.id}
        msg = response.json

        assert response.status_code == 200
        assert expected_msg == msg

    def test_get_product_by_id(self, client, product):
        """Test positive get product by id scenario"""
        # GIVEN product id
        # WHEN getting product from db
        # THEN return status code 200 and product data in json
        response = client.get(f'/shop/products/{product.id}')
        expected_product_name = 'test product'
        product_name = response.json.get('name')

        assert response.status_code == 200
        assert expected_product_name == product_name
