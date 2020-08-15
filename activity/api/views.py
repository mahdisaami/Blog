from rest_framework.generics import CreateAPIView

from activity.api.serializers import LikeCreateSerializer, CommentCreateSerializer
from content.models import Post


class LikeCreateAPIVew(CreateAPIView):
    serializer_class = LikeCreateSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        post = self.get_object()
        user = self.request.user
        serializer.save(post=post, user=user)


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        post = self.get_object()
        user = self.request.user
        serializer.save(post=post, user=user)
