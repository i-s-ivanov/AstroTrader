from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from telescope_shop.telescopes.forms import CommentForm
from telescope_shop.telescopes.models import Telescope, Comment
from telescope_shop.telescopes.views import TelescopeCreateView

UserModel = get_user_model()


class TestTelescopeListView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='test',
            password='test',
        )
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

    def test_telescope_list_url(self):
        response = self.client.get(reverse('telescope list'))
        self.assertEqual(response.status_code, 200)

    def test_telescope_list_with_one_item(self):
        response = self.client.get(reverse('telescope list'))
        posts = list(response.context['telescopes'])
        self.assertListEqual([self.telescope], posts)


class TestTelescopeDetailsView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='test',
            password='test',
        )
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

    def test_telescope_details_url(self):
        response = self.client.get(reverse('telescope details', args=[self.telescope.id]))
        self.assertEqual(response.status_code, 200)

    def test_context_data(self):
        self.comment = Comment.objects.create(
            name='test',
            text='test',
            telescope_id=self.telescope.id
        )
        response = self.client.get(reverse('telescope details', args=[self.telescope.id]))
        comments = list(response.context['comments'])
        self.assertListEqual([self.comment], comments)

        owner = response.context['telescope'].user_id
        self.assertTrue(owner, self.user.id)

        page = response.context['page_obj'].number
        self.assertEqual(page, 1)


class TestTelescopeCreateView(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(
            username='test',
            password='test',
        )

    def test_create_view_url(self):
        request = self.factory.get(reverse('create telescope'))
        request.user = self.user
        response = TelescopeCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_form_valid_on_create_view(self):
        data = {
            'make': 'test_make',
            'model': 'test_model',
            'description': 'test',
            'location': 'test_location',
            'contact_number': '01234',
            'image': 'path/to/image.png',
            'price': 100,
            'user': self.user,
        }

        request = self.factory.post(reverse('create telescope'), data=data)
        request.user = self.user

        response = TelescopeCreateView.as_view()(request)

        self.assertTrue(response.status_code, 200)


class TestTelescopeCreateView1(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='iskren',
            password='a1b2c3d4e5',
        )

    def test_create_telescope_post(self):
        telescope = Telescope.objects.create(
            make='test_make',
            model='test_model',
            description='test',
            location='test_location',
            contact_number='01234',
            image='path/to/image.png',
            price=100,
            user=self.user
        )
        self.client.force_login(self.user)

        response = self.client.get(reverse('telescope list'))
        user_post = list(response.context['telescopes'])
        self.assertListEqual([telescope], user_post)


class TestTelescopeUpdateView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='iskren',
            password='a1b2c3d4e5',
        )

    def test_update_telescope_post(self):
        self.client.force_login(self.user)
        telescope = Telescope.objects.create(
            make='test_make',
            model='test_model',
            description='test',
            location='test_location',
            contact_number='01234',
            image='path/to/image.png',
            price=100,
            user=self.user
        )
        response = self.client.get(reverse('telescope list'))
        user_telescopes = list(response.context['telescopes'])
        self.assertListEqual([telescope], user_telescopes)

        self.client.post(reverse('update telescope', args=[telescope.id]), data={
            'make': 'test',
            'model': 'test_model',
            'description': 'test',
            'location': 'test_location',
            'contact_number': '01234',
            'image': 'path/to/image.png',
            'price': 100,
            'user': self.user,
        })

        response = self.client.get(reverse('update telescope', args=[telescope.id]))
        user_telescopes = response.context['telescope']
        self.assertEqual(user_telescopes.make, 'test')


class TestCommentView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='iskren',
            password='a1b2c3d4e5',
        )

    def test_comment_view_without_comments(self):
        telescope = Telescope.objects.create(
            make='test_make',
            model='test_model',
            description='test',
            location='test_location',
            contact_number='01234',
            image='path/to/image.png',
            price=100,
            user=self.user
        )
        comment = Comment.objects.create(
            name='test',
            text='test',
            telescope_id=telescope.id
        )
        response = self.client.get(reverse('telescope details', kwargs={
            'pk': telescope.id
        }))
        comments = list(response.context['comments'])

        self.assertListEqual([comment], comments)
        self.assertTrue(isinstance(comments[0], Comment))