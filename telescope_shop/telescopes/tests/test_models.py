from django.contrib.auth import get_user_model
from django.test import TestCase

from telescope_shop.telescopes.models import Telescope, Comment

UserModel = get_user_model()


class TestTelescopeModel(TestCase):

    def setUp(self) -> None:
        self.telescope = Telescope.objects.create(
            make='test_make',
            model='test_model',
            description='test',
            location='test_location',
            contact_number='01234',
            image='path/to/image.png',
            price=100,
            user=UserModel.objects.create_user(
                username='test',
                password='test',
            )
        )

    def test_telescope_model_entry(self):
        data = self.telescope
        self.assertTrue(isinstance(data, Telescope))

    def test_telescope_model_return(self):
        data = self.telescope
        self.assertEqual(str(data), 'test_make | test_model')


class TestCommentModel(TestCase):

    def setUp(self) -> None:
        self.telescope = Telescope.objects.create(
            make='test_make',
            model='test_model',
            description='test',
            location='test_location',
            contact_number='01234',
            image='path/to/image.png',
            price=100,
            user=UserModel.objects.create_user(
                username='test',
                password='test',
            )
        )
        self.comment = Comment.objects.create(
            telescope=self.telescope,
            name='test_name',
            text='test_text',
        )

    def test_telescope_comment_return(self):
        data = self.comment
        self.assertEqual(str(data), 'test_make - test_name')

