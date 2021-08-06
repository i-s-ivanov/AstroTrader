from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class AstroTraderTestCase(TestCase):
    username = 'test'
    password = 'test'

    def assertListEmpty(self, l):
        return self.assertListEqual([], l)

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username=self.username,
            password=self.password,
        )
