from django.contrib.auth import get_user_model
from rest_framework import serializers

from author.models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Profile
        fields = ('avatar', 'phone_number', 'user')


class RegisterUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ("username", 'email', 'profile', 'password')

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        if profile['phone_number'] is None and profile['avatar'] is None:
            serializer = ProfileSerializer(data={'phone_number': None, 'avatar': None})
        elif profile['phone_number'] is None:
            serializer = ProfileSerializer(data={"avatar": profile["avatar"]})
        elif profile['avatar'] is None:
            serializer = ProfileSerializer(data={'phone_number': profile['phone_number']})
        else:
            serializer = ProfileSerializer(
                data={'phone_number': profile['phone_number'], 'avatar': profile['avatar']}
            )
        instance = super().create(validated_data)
        if serializer.is_valid():
            serializer.save(user=instance)
        return instance
