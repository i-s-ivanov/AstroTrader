from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase

from telescope_shop.accounts.models import Profile

UserModel = get_user_model()


class TestProfileModel(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test_name',
            password='test_password',
        ),
        self.profile = UserModel.objects.last().profile

    def test_profile_model_entry(self):
        data = self.profile
        self.assertTrue(isinstance(data, Profile))

    def test_profile_model_return(self):
        data = self.profile
        self.assertEqual(str(data), 'test_name')



