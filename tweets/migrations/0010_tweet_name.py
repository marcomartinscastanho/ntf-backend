# Generated by Django 4.2 on 2023-04-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_alter_tweet_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='name',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
