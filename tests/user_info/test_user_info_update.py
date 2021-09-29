import pytest

from fixtures.userinfo.model import UpdateUserInfoResponse, UpdateUserInfo


class TestUpdate:
    def test_user_info_update_with_valid_data(self, app, user_info):
        """
        1. Try to update user info
        2. Check that status code is 200
        3. Check response
        """
        data = UpdateUserInfo.random()
        res = app.user_info.update_user_info(
            user_id=user_info.uuid,
            data=data,
            header=user_info.header,
            type_response=UpdateUserInfoResponse
        )
        assert res.status_code == 200

    @pytest.mark.parametrize("uuid", ["ffddass", "@/&", -55, True])
    def test_user_info_update_with_invalid_id(self, app, user_info, uuid):
        """
        1. Try to update user info with invalid id
        2. Check that status code is 404
        """
        data = UpdateUserInfo.random()
        res = app.user_info.update_user_info(
            user_id=uuid,
            data=data,
            header=user_info.header,
            type_response=None
        )
        assert res.status_code == 404

    def test_none_exist_id_userinfo(self, app, user_info, uuid=1000):
        """
        1. Try to update user info with does not exist id
        2. Check that status code is 404
        """
        data = UpdateUserInfo.random()
        res = app.user_info.update_user_info(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 404

    """Должен выдавать 400 ошибку"""
    @pytest.mark.xfail
    def test_user_info_invalid_phone(self, app, user_info, phone="1" * 10000):
        """
        1. Try to update user info with invalid phone number
        2. Check that status code is 400
        """
        data = UpdateUserInfo.random()
        setattr(data, "phone", phone)
        res = app.user_info.update_user_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 400

    def test_update_user_info_wo_header(self, app, user_info):
        """
        1. Try to update user info without header
        2. Check that status code is 400
        """
        data = UpdateUserInfo.random()
        res = app.user_info.update_user_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=None,
        )
        assert res.status_code == 401

    def test_update_user_info_invalid_header(self, app, user_info):
        """
        1. Try to update user info with invalid header
        2. Check that status code is 400
        """
        data = UpdateUserInfo.random()
        header = {"Authorization": "JWT 895241"}
        res = app.user_info.update_user_info(
            user_id=user_info.uuid, data=data, type_response=None, header=header
        )
        assert res.status_code == 401
