from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
import markdown

from django.shortcuts import render
from .models import Post
from tag.models import Tag

def post_list(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'tags': tags})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    tags = Tag.objects.all()

    return render(request, 'post_detail.html', {'post': post, 'tags': tags})

def blog_index(request):
    return render(request, 'blog_index.html')