from django.db import models
from options.models import Tag, Blog
from tweets.models import Tweet


class Post(models.Model):
    RATINGS = (("F", "F"), ("O", "O"), ("M", "M"), ("X", "X"))
    comment = models.CharField(blank=True, max_length=500)
    tweet = models.ForeignKey(Tweet, blank=False, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    source = models.URLField()
    rating = models.CharField(max_length=8, choices=RATINGS, default='F')
    blog = models.ForeignKey(Blog, blank=False, on_delete=models.CASCADE, related_name="posts")
    queue = models.BooleanField(blank=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
