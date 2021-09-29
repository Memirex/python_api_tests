from requests import Response

from fixtures.register.model import RegisterUser
from fixtures.userinfo.model import UserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class UserInform(Validator):
    def __init__(self, app):
        self.app = app

    POST_USERINFO = "/user_info/{}"

    @log("Register new user")
    def add_user_info(self, user_id: int, data: UserInfo, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USERINFO.format(user_id)}",
            json=data.to_dict(),
            headers=header
        )
        return self.structure(response, type_response=type_response)
