# Generated by Django 4.2 on 2023-04-12 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=200)),
                ('source', models.URLField()),
                ('text', models.TextField(max_length=1000)),
                ('posted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TweetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thumb', models.URLField()),
                ('large', models.URLField()),
                ('is_published', models.BooleanField(default=False)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.tweet')),
            ],
        ),
    ]
