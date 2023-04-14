from rest_framework import serializers
from .models import Tweet, TweetImage


class TweetImageSerializer(serializers.HyperlinkedModelSerializer):
    tweet = serializers.ReadOnlyField(source='tweet.tid')

    class Meta:
        model = TweetImage
        fields = ['url', 'id', 'name', 'tweet', 'thumb', 'large', 'position', 'is_posted']


class ShortTweetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetImage
        fields = ['id', 'position', 'name',  'thumb', 'large']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, tweet):
        qs = TweetImage.objects.filter(post__isnull=True, tweet=tweet)
        serializer = ShortTweetImageSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Tweet
        fields = ['url', 'id', 'author', 'source', 'text', 'tweeted', 'images']


class ShortTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'source', 'text', 'tweeted']
