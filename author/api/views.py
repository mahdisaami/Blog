from rest_framework.generics import CreateAPIView

from author.api.serializers import RegisterUserSerializer


class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
