# post/models.py
from django.contrib.auth.models import User
from django.db import models
from mdeditor.fields import MDTextField

from tag.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = MDTextField(null=True, blank=True)
    content_preview = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_index_post = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.title


class TextAsset(models.Model):
    ASSET_TYPES = (
        ('logo', 'Logo'),
        ('copyright', 'Copyright'),
        ('about', 'About'),
        ('contact', 'Contact')
    )
    asset_type = models.CharField(max_length=50, choices=ASSET_TYPES)
    content = models.TextField()


def __str__(self):
    return f"{self.get_asset_type_display()}: {self.content[:50]}"
