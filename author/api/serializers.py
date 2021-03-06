from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from kombu import Queue
from rest_framework import serializers

from author.models import Profile
from author.tasks import send_welcoming_message
from content.api.serializers import PostListSerializer
from content.models import Post
from relation.models import Relation

User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)
    avatar = serializers.CharField(allow_null=True)
    phone_number = serializers.CharField(allow_null=True)

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
        password = make_password(validated_data['password'])
        validated_data['password'] = password
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
        send_welcoming_message.apply_async([validated_data['username'], ], Queue='low')
        if serializer.is_valid():
            serializer.save(user=instance)
        return instance


class UserListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()
    posts_quantity = serializers.SerializerMethodField()
    posts = PostListSerializer(many=True)
    followers = serializers.SerializerMethodField()
    followings = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('profile', 'username', 'email', 'followers', 'followings', 'posts_quantity', 'posts', )

    def get_posts_quantity(self, obj):
        post = Post.objects.filter(user=obj)
        quantity = post.count()
        return quantity

    def get_followers(self, obj):
        followers = Relation.objects.filter(to_user=obj)
        quantity = followers.count()
        return quantity

    def get_followings(self, obj):
        followings = Relation.objects.filter(from_user=obj)
        quantity = followings.count()
        return quantity


class UserLightSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()

    class Meta:
        model = User
        fields = ('profile', 'username', 'email')
