from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post
from posts.tasks import post_to_newtumbl


@receiver(post_save, sender=Post)
def send_post(sender, instance, created, **kwargs):
    if created:
        post_to_newtumbl.delay(post_id=instance.pk)
