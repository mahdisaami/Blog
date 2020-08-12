import django_filters
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from author.api.serializers import RegisterUserSerializer, UserListSerializer


User = get_user_model()


class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('username',)

    def get_queryset(self):
        queryset = User.objects.all().order_by('-date_joined')
        return queryset


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserListSerializer
    lookup_url_kwarg = 'username'
    lookup_field = 'username'
    queryset = User.objects.all()

