from django.shortcuts import render

from django.shortcuts import render
from .models import Post

def blog_preview(request):
    posts = Post.objects.all()
    return render(request, 'blog_preview.html', {'posts': posts})
