class TestAccountsPositive:
    """Test positive admin api scenarios"""

    def test_admin_user_create(self, client):
        """Test positive admin registration scenario"""
        # GIVEN admin data in json
        # WHEN admin data is saved in json
        # THEN return status code 201 and admin email
        admin_data = {'email': 'admin@admin.com', 'password': 'Test1234'}
        response = client.post('/admin_managing/create_admin', json=admin_data)
        user_email = response.json.get('user')['email']
        expected_email = 'admin@admin.com'

        assert response.status_code == 201
        assert user_email == expected_email

    def test_admin_user_login(self, client, admin):
        """Test positive admin login scenario"""
        # GIVEN admin credentials
        # WHEN authorizing admin
        # THEN return status code 200 and tokens for admin
        _, email, pwd = admin
        admin_data = {'email': email, 'password': pwd}
        response = client.post('/admin_managing/login_admin', json=admin_data)
        access_token = response.json.get('access')
        refresh_token = response.json.get('refresh')

        assert response.status_code == 200
        assert access_token
        assert refresh_token

    def test_create_category(self, client, token_admin):
        """Test admin create category"""
        # GIVEN category name
        # WHEN category is validated
        # THEN save category in db, return status code 201 and 'Category: Test was created' msg
        headers = {
            'Authorization': f'Bearer {token_admin}'
        }
        data = {'category': 'Test'}
        response = client.post('/admin_managing/create_category', json=data, headers=headers)
        expected_msg = {'message': 'Category: Test was created'}
        msg = response.json

        assert response.status_code == 201
        assert expected_msg == msg

    def test_get_admin_panel(self, client, token_admin):
        """Test get admin panel"""
        # GIVEN admin token
        # WHEN admin is authorized
        # THEN return status code 200 and admin panel
        headers = {
            'Authorization': f'Bearer {token_admin}'
        }
        response = client.get('/admin/', headers=headers)

        assert response.status_code == 200
