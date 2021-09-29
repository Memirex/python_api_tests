from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()

@attr.s
class Store(BaseClass):


    @staticmethod
    def random():
        address = Address(city=fake.city(), street=fake.street_name(), home_number=fake.building_number())
        return UserInfo(phone=fake.phone_number(), email=fake.email(), address=address)


@attr.s
class UserInfoResponse:
    message: str = attr.ib()
