# Generated by Django 5.0.1 on 2024-01-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_index_post',
            field=models.BooleanField(default=False),
        ),
    ]
