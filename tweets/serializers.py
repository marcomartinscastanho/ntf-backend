from rest_framework import serializers
from .models import Tweet, TweetImage


class TweetImageSerializer(serializers.HyperlinkedModelSerializer):
    tweet = serializers.ReadOnlyField(source='tweet.tid')

    class Meta:
        model = TweetImage
        fields = ['url', 'id', 'name', 'tweet', 'thumb', 'large', 'is_posted']


class ShortTweetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetImage
        fields = ['name',  'thumb', 'large']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    # images = serializers.HyperlinkedIdentityField(many=True, view_name='tweetimage-detail', read_only=True)
    images = ShortTweetImageSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ['url', 'id', 'author', 'tweet_id', 'source', 'text', 'tweeted', 'images']
