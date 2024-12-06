from django.db import models


class Tweet(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=1000, blank=True)
    source = models.URLField()
    text = models.TextField(max_length=1000, blank=True)
    tweeted = models.DateTimeField()

    @property
    def is_posted(self):
        # a tweet is posted if all its images are posted
        return all([img.is_posted for img in self.images.all()])

    class Meta:
        ordering = ["-tweeted"]


def thumbnail_path(instance, filename):
    return "tweet_images/thumbnails/{0}/{1}".format(instance.tweet.author, filename)


def large_image_path(instance, filename):
    return "tweet_images/large/{0}/{1}".format(instance.tweet.author, filename)


class TweetImage(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="images")
    position = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=thumbnail_path, null=True)
    large_image = models.ImageField(upload_to=large_image_path, null=True)
    post = models.ForeignKey("posts.Post", blank=True, null=True, on_delete=models.SET_NULL, related_name="images")

    class Meta:
        ordering = ["tweet", "position"]

    @property
    def is_posted(self):
        return self.post is not None
