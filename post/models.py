# post/models.py
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = MDTextField(null=True, blank=True)
    content_preview = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title