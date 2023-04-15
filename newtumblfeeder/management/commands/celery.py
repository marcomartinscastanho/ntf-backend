import shlex
import subprocess
from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    cmd = 'pkill -f celery'
    subprocess.call(shlex.split(cmd))
    cmd = 'celery -A newtumblfeeder worker -l info -B'
    subprocess.call(shlex.split(cmd))


class Command(BaseCommand):
    def handle(self, *args, **options):
        autoreload.run_with_reloader(restart_celery)
