

from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post
from .tasks import post_to_newtumbl


@receiver(post_save, sender=Post)
def send_post(sender, instance, created, **kwargs):
    if created:
        post_to_newtumbl.delay(post_id=instance.pk)
