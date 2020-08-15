from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from activity.models import Like, Comment


class LikeCreateSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Like
        fields = ('post', 'user')

    def create(self, validated_data):
        user = validated_data['user']
        post = validated_data['post']
        qs = Like.objects.filter(post=post, user=user)
        if qs.exists():
            raise ValidationError(_('Sorry you have already like this post'))
        super().create(validated_data)
        return validated_data


class CommentCreateSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'user', 'post', 'reply_to')

    def create(self, validated_data):
        if validated_data['reply_to'] is not None and validated_data['reply_to'].post != validated_data['post']:
            raise ValidationError(_('Sorry you can not do this'))
        super().create(validated_data)
        return validated_data


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'user', 'reply_to', 'created_time')
