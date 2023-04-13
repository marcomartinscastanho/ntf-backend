from django.db import models


class Tweet(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    author = models.CharField(max_length=100)
    source = models.URLField()
    text = models.TextField(max_length=1000, blank=True)
    tweeted = models.DateTimeField()

    @property
    def images(self):
        return self.tweetimage_set.all()

    @property
    def is_posted(self):
        # a tweet is posted if all its images are posted
        return all([img.is_posted for img in self.images])

    class Meta:
        ordering = ['tweeted']


class TweetImage(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=100)
    thumb = models.URLField()
    large = models.URLField()
    is_posted = models.BooleanField(default=False)

    class Meta:
        ordering = ['tweet', 'position']
