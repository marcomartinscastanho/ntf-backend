# Generated by Django 4.2 on 2023-04-16 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0008_remove_tweetimage_is_posted_tweetimage_post_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-tweeted']},
        ),
    ]
