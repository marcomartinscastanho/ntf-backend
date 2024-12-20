from django.db.models.signals import post_delete
from django.dispatch import receiver

from tweets.models import Tweet, TweetImage


@receiver(post_delete, sender=TweetImage)
def delete_tweet_if_no_images(sender, instance, **kwargs):
    try:
        images = TweetImage.objects.filter(tweet=instance.tweet)
        if len(images) == 0:
            tweet = Tweet.objects.get(pk=instance.tweet.id)
            tweet.delete()
    except Tweet.DoesNotExist:
        pass
