from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from author.api.serializers import UserLightSerializer
from relation.models import Relation


class RelationCreateSerializer(serializers.ModelSerializer):
    from_user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    to_user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Relation
        fields = ('from_user', 'to_user',)

    def create(self, validated_data):
        from_user = validated_data['from_user']
        to_user = validated_data['to_user']
        if from_user == to_user:
            raise ValidationError(_('Sorry you can not follow yourself!'))
        qs = Relation.objects.filter(from_user=from_user, to_user=to_user)
        if qs.exists():
            raise ValidationError(_('Sorry you have already followed this user'))
        relation = Relation.objects.create(from_user=from_user, to_user=to_user)
        return validated_data


class FollowersListSerializer(serializers.ModelSerializer):
    from_user = UserLightSerializer()

    class Meta:
        model = Relation
        fields = ('from_user', 'created_time')


class FollowingsListSerializer(serializers.ModelSerializer):
    to_user = UserLightSerializer()

    class Meta:
        model = Relation
        fields = ('to_user', 'created_time')