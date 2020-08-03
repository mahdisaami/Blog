from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers

from content.models import Post, Media, PostTag, Tag


class MediaListSerializer(serializers.ModelSerializer):
    media_type = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ('media_type', 'media_file')

    def get_media_type(self, obj):
        return obj.get_media_type_display()


class PostTagCreateSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)
    tag = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all())

    class Meta:
        model = PostTag
        fields = ('post', 'tag')


class PostTagListSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = PostTag
        fields = ('tag',)


class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # medias = MediaSerializer(many=True)
    post_tags = PostTagCreateSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'user', 'body', 'status', 'post_tags',)

    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return attrs

    def create(self, validated_data):
        tags = validated_data.pop('post_tags')
        instance = super().create(validated_data)
        # tags = tagged[0]
        for tag in tags:
            serializer = PostTagCreateSerializer(data={'tag': tag['tag']})
            if serializer.is_valid():
                serializer.save(post=instance)
        return instance


class PostListSerializer(serializers.ModelSerializer):
    medias = MediaListSerializer(many=True)
    post_tags = PostTagListSerializer(many=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'user', 'body', 'post_tags', 'medias')
