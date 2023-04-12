from django.db import models


class Tweet(models.Model):
    tid = models.CharField(max_length=200)
    source = models.URLField()
    text = models.TextField(max_length=1000)
    posted = models.DateTimeField()

    @property
    def images(self):
        return self.image_set.all()

    @property
    def is_published(self):
        # a tweet is published if all its images are published
        return all([img.is_published for img in self.images])


class TweetImage(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thumb = models.URLField()
    large = models.URLField()
    is_published = models.BooleanField(default=False)
