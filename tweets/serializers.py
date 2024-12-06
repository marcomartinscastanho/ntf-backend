from django.db import transaction
from rest_framework import serializers

from tweets.models import Tweet, TweetImage


class TweetImageSerializer(serializers.ModelSerializer):
    tweet = serializers.ReadOnlyField(source="tweet.tid")
    thumb = serializers.ImageField(max_length=None, use_url=True, source="thumbnail")
    large = serializers.ImageField(max_length=None, use_url=True, source="large_image")

    class Meta:
        model = TweetImage
        fields = ["id", "name", "tweet", "thumb", "large", "position"]


class ShortTweetImageSerializer(serializers.ModelSerializer):
    thumb = serializers.ImageField(max_length=None, use_url=True, source="thumbnail")
    large = serializers.ImageField(max_length=None, use_url=True, source="large_image")

    class Meta:
        model = TweetImage
        fields = ["id", "position", "name", "thumb", "large"]


class TweetSerializer(serializers.ModelSerializer):
    images = ShortTweetImageSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ["url", "id", "author", "name", "source", "text", "tweeted", "images"]

    def create(self, validated_data):
        with transaction.atomic():
            images_data = validated_data.pop("images")
            tweet = Tweet.objects.create(**validated_data)
            for pos, image_data in enumerate(images_data, 1):
                TweetImage.objects.create(tweet=tweet, **image_data, position=pos)
            return tweet
