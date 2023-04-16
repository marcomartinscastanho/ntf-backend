from rest_framework import serializers
from .models import Tweet, TweetImage


class FilterIsNotPostedListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(post__isnull=True)
        return super(FilterIsNotPostedListSerializer, self).to_representation(data)


class TweetImageSerializer(serializers.HyperlinkedModelSerializer):
    tweet = serializers.ReadOnlyField(source='tweet.tid')

    class Meta:
        model = TweetImage
        fields = ['url', 'id', 'name', 'tweet', 'thumb', 'large', 'position', 'is_posted']


class ShortTweetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetImage
        fields = ['id', 'position', 'name',  'thumb', 'large']
        list_serializer_class = FilterIsNotPostedListSerializer


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    images = ShortTweetImageSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ['url', 'id', 'author', 'source', 'text', 'tweeted', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        tweet = Tweet.objects.create(**validated_data)
        for pos, image_data in enumerate(images_data):
            TweetImage.objects.create(tweet=tweet, **image_data, position=pos+1)
        return tweet


class TweetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'source', 'text', 'tweeted', 'images']


class ShortTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'source', 'text', 'tweeted']
