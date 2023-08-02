from celery import shared_task
from celery.utils.log import get_task_logger
from .api import set_post_complete, set_post_compose, login, set_post_options, set_post_part_insert, set_post_part_update, set_post_part_update_comment, set_post_publish, set_post_queue, upload_with_binary, upload_with_url
from .models import Post

logger = get_task_logger(__name__)


@shared_task(name="post_to_newtumbl")
def post_to_newtumbl(post_id):
    post = Post.objects.prefetch_related('images').get(pk=post_id)
    try:
        session_token = login()
        post_ix = set_post_compose(session_token, post.blog.id)
        for image in post.images.all():
            part_ix = upload_with_binary(session_token, image.large, image.name)
            set_post_part_insert(session_token, post_ix, part_ix)
        set_post_part_update(session_token, post_ix)
        set_post_part_update_comment(session_token, post_ix, post.comment)
        set_post_options(session_token, post_ix, post.rating_code, post.source,
                         ' '.join([f'#{t.name}' for t in post.tags.all()]))
        set_post_complete(session_token, post_ix)
        if post.queue:
            set_post_queue(session_token, post_ix)
        else:
            set_post_publish(session_token, post_ix)
        logger.info("POSTED!")

        if post_ix:
            post.nt_post_id = post_ix
            post.save()
    except Exception as e:
        logger.error(e)


# when we start saving the login on the session, we have to implement a retry mechanism on this task
# in case the login has been lost, we need to login and retry the task
# TODO: to implement the retry mechanism, see: https://docs.celeryq.dev/en/stable/userguide/tasks.html#retrying
# something like this
@shared_task(bind=True)
def send_twitter_status(self, oauth, tweet):
    try:
        # all the parts of the task here...
        pass
    # FIXME: maybe try a more specific exception
    except Exception as exc:
        # TODO: login, then
        raise self.retry(exc=exc)
