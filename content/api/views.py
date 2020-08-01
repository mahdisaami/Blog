from rest_framework.generics import CreateAPIView

from content.api.serializers import CreatePostSerializer


class CreatePostAPIView(CreateAPIView):
    serializer_class = CreatePostSerializer
