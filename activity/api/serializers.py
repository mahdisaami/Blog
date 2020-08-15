from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from activity.models import Like


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
        instance = Like.objects.create(post=post, user=user)
        return validated_data
