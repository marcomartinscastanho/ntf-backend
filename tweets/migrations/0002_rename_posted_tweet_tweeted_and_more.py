# Generated by Django 4.2 on 2023-04-12 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='posted',
            new_name='tweeted',
        ),
        migrations.RenameField(
            model_name='tweetimage',
            old_name='is_published',
            new_name='is_posted',
        ),
    ]
