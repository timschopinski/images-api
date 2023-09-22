from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from images.tests.factories import UserFactory


class AdminViewTestCase(TestCase):

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )

    def test_user_list_view(self):
        self.client.login(username='admin', password='adminpassword')
        url = reverse('admin:auth_user_changelist')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_via_admin(self):
        url = reverse('admin:auth_user_add')
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_edit_user_profile_via_admin(self):
        user = UserFactory()
        self.client.login(username='admin', password='adminpassword')
        url = reverse('admin:auth_user_change', args=[user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
