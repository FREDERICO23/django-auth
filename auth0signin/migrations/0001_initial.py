# Generated by Django 3.2.6 on 2021-09-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('post_title', models.CharField(max_length=255)),
                ('post_description', models.TextField()),
                ('post_description_markdown', models.TextField(blank=True)),
                ('post_author', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
