import uuid

from django.db import models


class Blog(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50)
    name = models.SlugField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50)
    genres = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="subgenres")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def num_posts(self):
        return len(self.posts.all())
