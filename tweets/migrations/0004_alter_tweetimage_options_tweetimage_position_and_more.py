# Generated by Django 4.2 on 2023-04-12 18:20

from django.db import migrations, models


def set_positions(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    TweetImage = apps.get_model('tweets', 'TweetImage')
    db_alias = schema_editor.connection.alias

    tweet_id = -1
    position = 1
    for instance in TweetImage.objects.using(db_alias).all():
        if instance.tweet.id == tweet_id:
            position += 1
        else:
            position = 1

        instance.position = position
        instance.save()
        tweet_id = instance.tweet.id


class Migration(migrations.Migration):
    dependencies = [
        ('tweets', '0003_alter_tweet_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetimage',
            name='position',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.RunPython(set_positions),
        migrations.AlterModelOptions(
            name='tweetimage',
            options={'ordering': ['tweet', 'position']},
        ),
    ]
