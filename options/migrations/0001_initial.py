# Generated by Django 4.2 on 2023-04-14 13:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('name', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('genres', models.ManyToManyField(blank=True, related_name='subgenres', to='options.tag')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
