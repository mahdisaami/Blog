from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from activity.models import Comment
from content.models import Post

User = get_user_model()


class CreateCommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Test", password="QAZwsx!@#456", email='mahdi@email.com')
        self.post = Post.objects.create(title='TestCase', user=self.user)
        self.client = APIClient()

    def test_post_existence(self):
        self.assertTrue(Post.objects.exists())
        self.assertTrue(User.objects.exists())

    def test_comment_creation_api_view(self):
        comment_data = {'text': 'simple comment', 'post': self.post.id, 'reply_to': None}
        self.client.force_authenticate(user=self.user)
        result = self.client.post('/api/activity/comment/post{}'.format(self.post.id), comment_data, format='json')
        self.assertEqual(result.status_code, 201, f"status code is wrong {result}")
        self.assertEqual(Comment.objects.count(), 1)


class CreateLikeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='Test', password=123)
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test', user=self.user)

    def test_create_like(self):
        like_data = {
            'user': self.user.id,
            'post': self.post.id,
        }
        result = self.client.post('/api/activity/like/post{}'.format(self.post.id), like_data, format='json')
        self.assertEqual(result.status_code, 201, f'status code is wrong {result}')










