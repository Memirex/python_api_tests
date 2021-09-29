from faker import Faker
import attr

from fixtures.base import BaseClass
from fixtures.userinfo.model import UserInfo

fake = Faker()


@attr.s
class Login(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return Login(username=fake.email(), password=fake.password())


@attr.s
class LoginUserResponse:
    access_token: str = attr.ib()


@attr.s
class UserType:
    header: dict = attr.ib()
    uuid: int = attr.ib()
    user_data: UserInfo = attr.ib(default=None)
