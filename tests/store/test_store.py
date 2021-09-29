

class TestStore:
    def test_store_with_valid_data(self, app, auth_user):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        4. Authorization with random data
        5. Check that status code is 200
        6. Add user info.
        7. Check that status code is 200
        3. Check response
        """
        data = UserInfo.random()
        us_info = app.user_info.add_user_info(data=data, user_id=auth_user.uuid,
                                              header=auth_user.header, type_response=UserInfoResponse)
        assert us_info.status_code == 200
        assert us_info.data.message == ResponseText.MESSAGE_ADD_USER_INFO