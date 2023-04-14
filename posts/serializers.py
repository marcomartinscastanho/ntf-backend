from rest_framework import serializers
from .models import Post
from options.models import Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'comment', 'tweet', 'tags', 'source', 'rating', 'blog', 'images']

    def to_internal_value(self, data):
        for tag in data['tags']:
            Tag.objects.get_or_create(pk=tag)
        return super().to_internal_value(data)
