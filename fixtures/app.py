from fixtures.auth.api import LogIn
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.userinfo.api import UserInform


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.login = LogIn(self)
        self.user_info = UserInform(self)
