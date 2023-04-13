from django.db import models
import uuid


class Blog(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50)
    name = models.SlugField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50)
    genres = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # @property
    # def num_posts(self):
    #     return len(self.posts())

    # @property
    # def posts(self):
    #     return self.posts_set.all()
