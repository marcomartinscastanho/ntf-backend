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
    nt_post_id = models.CharField(blank=True, null=True, max_length=16)

    @property
    def rating_code(self):
        return rating_code_converter(self.rating)

    @property
    def is_posted(self):
        return self.nt_post_id != None


def rating_code_converter(r: str) -> int:
    return 1 + [rating[0] for rating in Post.RATINGS].index(r)
