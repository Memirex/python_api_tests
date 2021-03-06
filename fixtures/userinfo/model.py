from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Address(BaseClass):
    city: str = attr.ib(default=None)
    street: str = attr.ib(default=None)
    home_number: str = attr.ib(default=None)


@attr.s
class UserInfo(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address() = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(city=fake.city(), street=fake.street_name(), home_number=fake.building_number())
        return UserInfo(phone=fake.phone_number(), email=fake.email(), address=address)


@attr.s
class UpdateUserInfo(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address() = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(city=fake.city(), street=fake.street_name(), home_number=fake.building_number())
        return UserInfo(phone=fake.phone_number(), email=fake.email(), address=address)

@attr.s
class AddUserInfoResponse:
    message: str = attr.ib()


@attr.s
class UpdateUserInfoResponse:
    message: str = attr.ib()
