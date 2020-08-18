from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from activity.api.serializers import LikeCreateSerializer, CommentCreateSerializer, CommentListSerializer
from activity.models import Comment
from activity.paginations import CommentListPagination
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
    authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        post = self.get_object()
        user = self.request.user
        serializer.save(post=post, user=user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all().order_by('-created_time')
    authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = CommentListPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        comments = queryset.filter(post=self.kwargs['pk'])
        return comments
