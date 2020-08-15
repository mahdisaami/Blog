from rest_framework.generics import CreateAPIView, ListAPIView

from activity.api.serializers import LikeCreateSerializer, CommentCreateSerializer, CommentListSerializer
from activity.models import Comment
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


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all().order_by('-created_time')

    def get_queryset(self):
        queryset = super().get_queryset()
        comments = queryset.filter(post=self.kwargs['pk'])
        return comments
