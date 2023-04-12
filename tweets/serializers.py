from rest_framework import serializers
from .models import Tweet, TweetImage


class TweetImageSerializer(serializers.HyperlinkedModelSerializer):
    tweet = serializers.ReadOnlyField(source='tweet.tid')

    class Meta:
        model = TweetImage
        fields = ['url', 'id', 'name', 'tweet', 'thumb', 'large', 'is_posted']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedIdentityField(many=True, view_name='tweetimage-detail', read_only=True)
    # images = TweetImageSerializer(read_only=True, required=False, many=True)

    class Meta:
        model = Tweet
        fields = ['url', 'id', 'tid', 'source', 'text', 'tweeted', 'images']
