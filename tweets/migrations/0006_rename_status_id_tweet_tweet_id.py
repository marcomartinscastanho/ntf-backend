# Generated by Django 4.2 on 2023-04-13 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_alter_tweet_options_remove_tweet_tid_tweet_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='status_id',
            new_name='tweet_id',
        ),
    ]
