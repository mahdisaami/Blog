from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from relation.api.serializers import RelationCreateSerializer

User = get_user_model()


class FollowUserAPIView(CreateAPIView):
    serializer_class = RelationCreateSerializer
    lookup_url_kwarg = 'username'
    lookup_field = 'username'
    queryset = User.objects.all()

    def perform_create(self, serializer):
        target_user = self.get_object()
        if target_user is not None:
            serializer.save(from_user=self.request.user, to_user=target_user)
