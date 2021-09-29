import attr

from fixtures.base import BaseClass
from fixtures.register.model import RegisterUser
from fixtures.userinfo.model import UserInfo


@attr.s
class MessageResponse:
    message: str = attr.ib()


@attr.s
class UserStore(BaseClass):
    user: RegisterUser = attr.ib(default=None)
    user_uuid: int = attr.ib(default=None)
    header: dict = attr.ib(default=None)
    user_info: UserInfo = attr.ib(default=None)
    store: str = attr.ib(default=None)


@attr.s
class AuthInvalidResponse:
    description: str = attr.ib()
    error: str = attr.ib()
    status_code: int = attr.ib()
