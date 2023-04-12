from rest_framework import serializers
from .models import Tweet, TweetImage


class TweetImageSerializer(serializers.ModelSerializer):
    tweet = serializers.ReadOnlyField(source='tweet.tid')

    class Meta:
        model = TweetImage
        fields = ['id', 'name', 'tweet', 'thumb', 'large', 'is_posted']


class TweetSerializer(serializers.ModelSerializer):
    # images = serializers.PrimaryKeyRelatedField(many=True, queryset=TweetImage.objects.all())
    images = TweetImageSerializer(read_only=True, required=False, many=True)

    class Meta:
        model = Tweet
        fields = ['tid', 'source', 'text', 'tweeted', 'images']
