class TestAccountsPositive:
    """Test positive scenario accounts managing"""

    def test_user_create(self, app, fake_db):
        """Test positive user registration scenario"""
        # GIVEN user's email and password in json format
        # WHEN user's data is saved in db
        # THEN return status code 201 and user's email
        user_data = {'email': 'test@test.com', 'password': 'Test1234'}
        response = app.test_client().post('/auth/register', json=user_data)
        user_email = response.json.get('user')['email']
        expected_email = 'test@test.com'

        assert response.status_code == 201
        assert user_email == expected_email

    def test_user_login(self, app, fake_db, create_user):
        """Test positive user login scenario"""
        # GIVEN user's email and password in json format
        # WHEN user sends request with his data
        # THEN return status code 200 and tokens for user
        _, email, pwd = create_user
        user_data = {'email': email, 'password': pwd}
        response = app.test_client().post('/auth/login', json=user_data)
        access_token = response.json.get('access')
        refresh_token = response.json.get('refresh')

        assert response.status_code == 200
        assert access_token
        assert refresh_token

    def test_accounts_info(self, app, fake_db, create_token):
        """Test user accounts info endpoint"""
        # GIVEN user's access token
        # WHEN user found by token
        # THEN return user profile info
        headers = {
            'Authorization': f'Bearer {create_token}'
        }
        response = app.test_client().get('/auth/info', headers=headers)
        expected_msg = {'user': {
            'email': 'test@test.com',
            'products': []
        }}
        msg = response.json

        assert response.status_code == 200
        assert expected_msg == msg
