from rest_framework.generics import CreateAPIView

from activity.api.serializers import LikeCreateSerializer
from content.models import Post


class LikeAPIVew(CreateAPIView):
    serializer_class = LikeCreateSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        post = self.get_object()
        user = self.request.user
        serializer.save(post=post, user=user)
