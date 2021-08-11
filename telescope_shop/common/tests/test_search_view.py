from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from telescope_shop.telescopes.models import Telescope

UserModel = get_user_model()


class TestSearchView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='iskren',
            password='a1b2c3d4e5',
        )

    def test_search_view_results(self):
        self.telescope = Telescope.objects.create(
            make='test_make',
            model='test_model',
            description='test',
            location='test_location',
            contact_number='01234',
            image='path/to/image.png',
            price=100,
            user=self.user
        )
        self.telescope.save()
        response = self.client.get(reverse('search results'), data={
            'q': 'test_make'
        })
        telescope = response.context['telescope']
        self.assertEqual(telescope.make, self.telescope.make)
        self.assertEqual(response.status_code, 200)
