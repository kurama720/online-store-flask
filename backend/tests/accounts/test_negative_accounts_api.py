class TestAccountsNegative:
    """Test negative scenario accounts managing"""

    def test_invalid_register_email(self, app, fake_db):
        """Test invalid email while user registration"""
        # GIVEN invalid user's email
        # WHEN validating user's data
        # THEN return status code 400 and 'Email is not valid' msg
        user_data = {'email': 'test', 'password': 'Test1234'}
        response = app.test_client().post('/auth/register', json=user_data)
        expected_msg = 'Email is not valid'
        msg = response.json.get('error')

        assert expected_msg == msg
        assert response.status_code == 400

    def test_invalid_register_password(self, app, fake_db):
        """Test invalid password while user registration"""
        # GIVEN invalid user's password
        # WHEN validating user's data
        # THEN return status code 400 and 'Password is too short' msg
        user_data = {'email': 'test@test.com', 'password': '1234'}
        response = app.test_client().post('/auth/register', json=user_data)
        expected_msg = 'Password is too short'
        msg = response.json.get('error')

        assert expected_msg == msg
        assert response.status_code == 400

    def test_wrong_credentials_unregistered_user(self, app, fake_db):
        """Test logining unregistered user"""
        # GIVEN unregistered user
        # WHEN authorizing an unregistered user
        # THEN return status code 404
        user_data = {'email': 'test2@test.com', 'password': 'Test1234'}
        response = app.test_client().post('/auth/login', json=user_data)

        assert response.status_code == 404

    def test_wrong_credentials_registered_user(self, app, fake_db):
        """Test wrong credentials of registered user"""
        # GIVEN wrong credentials
        # WHEN authorizing a registered user
        # THEN return status code 401 and 'Wrong credentials' msg
        user_data = {'email': 'test@test.com', 'password': 'Test1234'}
        wrong_credentials = {'email': 'test@test.com', 'password': '1234Test'}
        app.test_client().post('/auth/register', json=user_data)
        response = app.test_client().post('/auth/login', json=wrong_credentials)
        expected_msg = 'Wrong credentials'
        msg = response.json.get('error')

        assert expected_msg == msg
        assert response.status_code == 401

    def test_wrong_token_accounts_info(self, app, fake_db):
        """Test invalid token on accounts info endpoint"""
        # GIVEN invalid token
        # WHEN authorizing user
        # THEN return status code 422 and 'Not enough segments' msg
        token = 'token'
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = app.test_client().get('/auth/info', headers=headers)
        expected_msg = 'Not enough segments'
        msg = response.json.get('msg')

        assert response.status_code == 422
        assert expected_msg == msg
