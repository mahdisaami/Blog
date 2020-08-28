import json

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework.test import APIClient

User = get_user_model()


class CreatePostTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='Test', password=123)

    def test_create_post(self):
        post_data = json.dumps({
            'title': 'Test Post',
            'user': self.user.id,
            'post_tags': []
        })
        self.client.force_authenticate(user=self.user)
        result = self.client.post(path='/api/content/posts/', data=post_data, content_type='application/json')
        self.assertEqual(result.status_code, 201)

    def test_get_posts(self):
        result = self.client.get(path='/api/content/posts/', content_type='application/json')
        self.assertEqual(result.status_code, 200)
