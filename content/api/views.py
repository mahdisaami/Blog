import django_filters
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, ListAPIView

from content.api.serializers import PostCreateSerializer, PostListSerializer
from content.models import Post


class PostCreateListAPIView(ListCreateAPIView):
    serializer_class = PostListSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('title', 'user__username', 'post_tags__tag__title')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PostCreateSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by('-created_time')
        return queryset

