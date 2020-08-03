from rest_framework.generics import CreateAPIView, ListCreateAPIView

from content.api.serializers import PostCreateSerializer, PostListSerializer
from content.models import Post


class PostCreateListAPIView(ListCreateAPIView):
    serializer_class = PostListSerializer


    def get_serializer_class(self):
        if self.request.method == "POST":
            return PostCreateSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by('-created_time')
        return queryset
