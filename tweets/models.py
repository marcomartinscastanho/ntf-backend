from django.db import models


class Tweet(models.Model):
    tid = models.CharField(max_length=200)
    source = models.URLField()
    text = models.TextField(max_length=1000)
    tweeted = models.DateTimeField()

    @property
    def images(self):
        return self.tweetimage_set.all()

    @property
    def is_posted(self):
        # a tweet is posted if all its images are posted
        return all([img.is_posted for img in self.images])

    # class Meta:
    #     ordering = ['created']


class TweetImage(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thumb = models.URLField()
    large = models.URLField()
    is_posted = models.BooleanField(default=False)
