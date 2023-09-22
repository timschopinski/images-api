import io
from django.test import TestCase
from django.urls import reverse
from images.tests.factories import UserFactory
from PIL import Image as IMG


class ImageTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    @staticmethod
    def generate_photo_file(file_format: str):
        file = io.BytesIO()
        image = IMG.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, file_format)
        file.name = 'test.' + file_format
        file.seek(0)
        return file

    def test_image_upload(self):
        url = reverse('image-list')
        image = self.generate_photo_file('png')
        response = self.client.post(url, {'image': image})
        self.assertEqual(response.status_code, 201)

    def test_wrong_image_format_validation(self):
        url = reverse('image-list')
        unsupported_image = self.generate_photo_file('webp')
        response = self.client.post(url, {'image': unsupported_image})
        self.assertEqual(response.status_code, 400)
        expected_response = {
            'image': [
                'Only PNG,JPG,JPEG formats are supported.'
            ]
        }
        self.assertEqual(response.json(), expected_response)
