from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from activity.models import Comment
from content.models import Post

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        comment_count = options['count']
        user = User.objects.filter(username='load_comments').first()
        if user is None:
            user = User.objects.create_user(username='load_comments', email='test@email.com', password='QAZwsx!@#456')
        post = Post.objects.filter(user=user).first()
        if post is None:
            post = Post.objects.create(user=user, title="Create Test Comments")

        for _ in range(comment_count):
            instance = Comment.objects.create(text='Test', post=post, user=user)
            print('Comment number {} added'.format(instance.pk))
