# Generated by Django 5.0.1 on 2024-01-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_content_preview_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_preview',
            field=models.TextField(blank=True, null=True),
        ),
    ]
