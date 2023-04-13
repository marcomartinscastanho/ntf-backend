from rest_framework import serializers
from .models import Blog, Genre, Tag


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id',  'name']


# FIXME: I don't think this will be needed
# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ['id',  'name']


class TagSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tag
        fields = ['name', 'genres']
