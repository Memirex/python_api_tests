from requests import Response

from fixtures.auth.model import Login
from fixtures.userinfo.model import UserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class LogIn(Validator):
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    @log("Authorization user")
    def login(self, data: Login, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth/authUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTH}",
            json=data.to_dict(),
            headers=header
        )
        return self.structure(response, type_response=type_response)
