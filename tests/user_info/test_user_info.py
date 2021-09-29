from fixtures.common_models import AuthInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.userinfo.model import UserInfo, AddUserInfoResponse


class TestUserInfo:
    def test_user_info_with_valid_data(self, app, auth_user):
        """
        1. Try to add user info.
        2. Check that status code is 200
        3. Check response
        """
        data = UserInfo.random()
        us_info = app.user_info.add_user_info(data=data, user_id=auth_user.uuid,
                                              header=auth_user.header, type_response=AddUserInfoResponse)
        assert us_info.status_code == 200
        assert us_info.data.message == ResponseText.MESSAGE_ADD_USER_INFO

    def test_user_info_without_header(self, app, auth_user):
        """
        1. Try to add user info without header
        2. Check that status code is 401
        3. Check response
        """
        data = UserInfo.random()
        us_info = app.user_info.add_user_info(data=data, user_id=auth_user.uuid,
                                              header=None, type_response=AuthInvalidResponse)
        assert us_info.status_code == 401, "Check status code"
        assert us_info.data.description == ResponseText.DESCRIPTION_AUTH_ERROR
        assert us_info.data.error == ResponseText.ERROR_AUTH_TEXT
        assert us_info.data.status_code == 401, "Check status code"

    def test_add_user_with_none_exist_user_id(
            self, app, auth_user, none_exist_user=1000
    ):
        """
        1. Try to add user info with none exist user id
        2. Check that status code is 404
        3. Check response
        """
        data = UserInfo.random()
        us_info = app.user_info.add_user_info(
            user_id=none_exist_user,
            data=data,
            header=auth_user.header,
            type_response=MessageResponse,
        )
        assert us_info.status_code == 404, "Check status code"
        assert us_info.data.message == ResponseText.MESSAGE_USER_NOT_FOUND
