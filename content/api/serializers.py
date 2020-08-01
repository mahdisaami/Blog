from rest_framework import serializers

from content.models import Post, Media, PostTag, Tag


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ('post', 'media_type', 'media_file')


class PostTagSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = PostTag
        fields = ('post', 'tag')


class CreatePostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # medias = MediaSerializer(many=True)
    post_tags = PostTagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'status', 'post_tags', 'user')

    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return attrs

    def create(self, validated_data):
        tags = validated_data.pop('post_tags')
        instance = super().create(validated_data)
        for tag in tags:
            serializer = PostTagSerializer(data={'tag': tag['tag'].pk})
            if serializer.is_valid():
                serializer.save(post=instance)
        return instance



