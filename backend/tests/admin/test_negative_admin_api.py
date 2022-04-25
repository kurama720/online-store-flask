class TestAccountsNegative:
    """Test negative admin api scenarios"""

    def test_invalid_register_email(self, client):
        """Test invalid email while user registration"""
        # GIVEN invalid admin email
        # WHEN validating admin data
        # THEN return status code 400 and 'Email is not valid' msg
        admin_data = {'email': 'test', 'password': 'Test1234'}
        response = client.post('/admin_managing/create_admin', json=admin_data)
        expected_msg = 'Email is not valid'
        msg = response.json.get('error')

        assert expected_msg == msg
        assert response.status_code == 400

    def test_invalid_register_password(self, client):
        """Test invalid password while admin registration"""
        # GIVEN invalid admin password
        # WHEN validating admin data
        # THEN return status code 400 and 'Password is too short' msg
        user_data = {'email': 'test@test.com', 'password': '1234'}
        response = client.post('/admin_managing/create_admin', json=user_data)
        expected_msg = 'Password is too short'
        msg = response.json.get('error')

        assert expected_msg == msg
        assert response.status_code == 400

    def test_duplicate_admin_email(self, client, admin):
        """Test duplicate user email"""
        # GIVEN duplicate admin email
        # WHEN validating admin data
        # THEN return status code 409 and 'Email already exists' msg
        _, email, _ = admin
        admin_data = {'email': email, 'password': 'Test1234'}
        response = client.post('/admin_managing/create_admin', json=admin_data)
        expected_msg = {'error': 'Email already exists'}
        msg = response.json

        assert expected_msg == msg
        assert response.status_code == 409

    def test_login_unregistered_admin(self, client):
        """Test logining unregistered admin"""
        # GIVEN unregistered admin
        # WHEN authorizing an unregistered user
        # THEN return status code 404
        admin_data = {'email': 'admin2@admin.com', 'password': 'Test1234'}
        response = client.post('/admin_managing/login_admin', json=admin_data)

        assert response.status_code == 404

    def test_wrong_credentials_registered_user(self, client, admin):
        """Test wrong credentials of registered admin"""
        # GIVEN wrong credentials
        # WHEN authorizing a registered admin
        # THEN return status code 401 and 'Wrong credentials' msg
        _, email, pwd = admin
        wrong_credentials = {'email': email, 'password': '1234Test'}
        response = client.post('/admin_managing/login_admin', json=wrong_credentials)
        expected_msg = 'Wrong credentials'
        msg = response.json.get('error')

        assert expected_msg == msg
        assert response.status_code == 401

    def test_create_duplicate_category(self, client, token_admin, category):
        """Test admin create duplicate category"""
        # GIVEN duplicate category name
        # WHEN category is validated
        # THEN return status code 409 and 'CategoryListItem already exists' msg
        headers = {
            'Authorization': f'Bearer {token_admin}'
        }
        data = {'category': category.name}
        response = client.post('/admin_managing/create_category', json=data, headers=headers)
        expected_msg = {'message': 'CategoryListItem already exists'}
        msg = response.json

        assert response.status_code == 409
        assert expected_msg == msg

    def test_get_admin_panel_by_user(self, client, token_user):
        """Test get admin panel by a common user"""
        # GIVEN user token
        # WHEN user is authorized
        # THEN return status code 403
        headers = {
            'Authorization': f'Bearer {token_user}'
        }
        response = client.get('/admin/', headers=headers)

        assert response.status_code == 403
