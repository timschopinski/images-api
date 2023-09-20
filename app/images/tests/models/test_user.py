from django.test import TestCase
from images.tests.factories import UserFactory
from images.models import UserProfile


class UserTestCase(TestCase):

    def test_create_user_with_profile(self):
        user = UserFactory()
        self.assertEqual(UserProfile.objects.filter(user=user).count(), 1)

    def tearDown(self):
        pass
