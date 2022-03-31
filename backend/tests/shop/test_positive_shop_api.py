class TestShopPositive:

    def test_upload_product(self, app, fake_db, create_token):
        """Test positive product upload scenario"""
        # GIVEN product data
        # WHEN save product in db
        # THEN return status code 201 and product's name
        product_data = {'name': 'product', 'description': 'test product', 'price': 2.49}
        headers = {
            'Authorization': f'Bearer {create_token}'
        }
        response = app.test_client().post('/shop/upload_product', json=product_data, headers=headers)
        expected_msg = {'Product': 'product', 'message': 'Product uploaded'}
        msg = response.json

        assert response.status_code == 201
        assert expected_msg == msg

    def test_get_product_list(self, app, fake_db, create_product):
        """Test positive product list scenario"""
        # WHEN GET request to the endpoint
        # THEN return status code 200 and a list with one product
        response = app.test_client().get('/shop/products')
        expected_msg = 'test product'
        msg = response.json.get('products')[0]['name']

        assert response.status_code == 200
        assert len(response.json) == 1
        assert expected_msg == msg

    def test_delete_product(self, app, fake_db, create_token, create_product):
        """Test positive product delete scenario"""
        # GIVEN product id
        # WHEN deleting product from bd
        # THEN return status code 200 and 'Product was deleted' msg
        headers = {
            'Authorization': f'Bearer {create_token}'
        }
        response = app.test_client().delete(f'/shop/delete_product/{create_product.id}', headers=headers)
        expected_msg = 'Product was deleted'
        msg = response.json.get('message')

        assert response.status_code == 200
        assert expected_msg == msg

    def test_update_product(self, app, fake_db, create_token, create_product):
        """Test positive product update scenario"""
        # GIVEN product id and data to update
        # WHEN updating data of the product
        # THEN return status code 200 and product new data json
        headers = {
            'Authorization': f'Bearer {create_token}'
        }
        data_to_update = {'name': 'not a testing product', 'description': 'not a tasty product', 'price': 0}
        response = app.test_client().put(f'/shop/update_product/{create_product.id}',
                                         json=data_to_update, headers=headers)
        expected_msg = {'category': None, 'description': 'not a tasty product',
                        'price': 0, 'name': 'not a testing product', 'id': create_product.id}
        msg = response.json

        assert response.status_code == 200
        assert expected_msg == msg

    def test_get_product_by_id(self, app , fake_db, create_product):
        """Test positive get product by id scenario"""
        # GIVEN product id
        # WHEN getting product from db
        # THEN return status code 200 and product data in json
        response = app.test_client().get(f'/shop/products/{create_product.id}')
        expected_product_name = 'test product'
        product_name = response.json.get('name')

        assert response.status_code == 200
        assert expected_product_name == product_name
