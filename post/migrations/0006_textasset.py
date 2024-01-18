# Generated by Django 5.0.1 on 2024-01-17 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_is_index_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(choices=[('logo', 'Logo'), ('copyright', 'Copyright'), ('about', 'About'), ('contact', 'Contact')], max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
