from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

User = get_user_model()


class CreateUserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password=1212)

    def test_create_user(self):
        user_data = {
            "username": "TestUser",
            "email": "info@gmail.com",
            "profile": {
                "avatar": None,
                "phone_number": None},
            "password": "7784dfs"
        }
        result = self.client.post('/api/user/create/', user_data, format='json')
        self.assertEqual(result.status_code, 201)

    def test_get_users(self):
        result = self.client.get('/api/user/list/', format='json')
        self.assertEqual(result.status_code, 200)

    def test_get_specific_user(self):
        result = self.client.get('/api/user/{}/'.format(self.user.username))
        self.assertEqual(result.status_code, 200)
