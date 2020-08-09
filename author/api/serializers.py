from django.contrib.auth import get_user_model
from rest_framework import serializers

from author.models import Profile
from content.models import Post

User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Profile
        fields = ('avatar', 'phone_number', 'user')


class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('avatar', 'bio')


class RegisterUserSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer()

    class Meta:
        model = User
        fields = ("username", 'email', 'profile', 'password')

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        if profile['phone_number'] is None and profile['avatar'] is None:
            serializer = ProfileCreateSerializer(data={'phone_number': None, 'avatar': None})
        elif profile['phone_number'] is None:
            serializer = ProfileCreateSerializer(data={"avatar": profile["avatar"]})
        elif profile['avatar'] is None:
            serializer = ProfileCreateSerializer(data={'phone_number': profile['phone_number']})
        else:
            serializer = ProfileCreateSerializer(
                data={'phone_number': profile['phone_number'], 'avatar': profile['avatar']}
            )
        instance = super().create(validated_data)
        if serializer.is_valid():
            serializer.save(user=instance)
        return instance


class UserListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()
    posts_quantity = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('profile', 'username', 'email', 'posts_quantity')

    def get_posts_quantity(self, obj):
        post = Post.objects.filter(user=obj)
        quantity = post.count()
        return quantity
