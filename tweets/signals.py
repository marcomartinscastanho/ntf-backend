

from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import TweetImage, Tweet


@receiver(post_delete, sender=TweetImage)
def delete_tweet_if_no_images(sender, instance, **kwargs):
    images = TweetImage.objects.filter(tweet=instance.tweet)
    if len(images) == 0:
        tweet = Tweet.objects.get(pk=instance.tweet.id)
        tweet.delete()
