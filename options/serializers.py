from rest_framework import serializers

from options.models import Blog, Tag


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "name"]


class TagSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    num_posts = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = ["name", "genres", "num_posts"]
