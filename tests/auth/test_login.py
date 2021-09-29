from fixtures.auth.model import Login
from fixtures.common_models import AuthInvalidResponse
from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse


class TestRegisterUser:
    def test_login_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        4. Authorization with random data
        5. Check that status code is 200
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER
        res_data = app.login.login(data=data)
        assert res_data.status_code == 200

    def test_auth_user_with_random_data(self, app):
        """
        1. Try to auth user with empty random data
        2. Check that status code is 401
        3. Check response
        """
        data = Login.random()
        res = app.login.login(data=data, type_response=AuthInvalidResponse)
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTH
        assert res.data.error == ResponseText.ERROR_AUTH
        assert res.data.status_code == 401, "Check status code"
