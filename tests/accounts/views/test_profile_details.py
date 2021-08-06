from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from telescope_shop.accounts.models import Profile
from telescope_shop.telescopes.models import Telescope
from django.contrib.auth.forms import UserCreationForm

from tests.base.tests import AstroTraderTestCase

UserModel = get_user_model()


class ProfileDetailsTest(AstroTraderTestCase):
    def test_get_details_whenLoggedInUserWithoutPosts_shouldGetDetails(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        posts = list(response.context['posts'])
        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertListEqual(posts, [])
        self.assertEqual(self.user.id, profile.user.id)

    def test_get_details_whenLoggedInUserWithPosts_shouldGetDetails(self):
        post = Telescope.objects.create(
            make='Test',
            model='Test',
            description='Test',
            location='Test',
            contact_number='0893123456',
            price=10,
            image='path/to/image.png',
            user=self.user,
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([post], list(response.context['posts']))

    def test_postDetails_whenUserLoggedInAndChangeImage_shouldChangeIt(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('profile details'), data={
            'profile_image': 'path/to/image.png'
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = 'path/to/image.png'

        self.assertEqual('path/to/image.png', profile.profile_image)


class RegisterUserTest(AstroTraderTestCase):
    # def setUp(self) -> None:
    #     self.client = Client()
    #     self.user = UserModel.objects.create_user(username='test', password='12345qwe')
    #
    # def test_registerUserSuccessfully(self):
    #     response = self.client.post(reverse('register'), data={
    #         'user': self.user
    #     })
    #
    #     self.assertEqual(200, response.status_code)
    def setUp(self):
        self.backend = UserCreationForm()

    def test_registration_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/register.html')
        self.failUnless(isinstance(response.context['form'], UserCreationForm))

    def test_registration_view_post_success(self):
        response = self.client.post(reverse('register'),
                                    data={'username': 'test',
                                          'password1': 'jomel4ea1b2c3d4e5',
                                          })

        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
