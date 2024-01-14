from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
import markdown

from django.shortcuts import render
from .models import Post

def blog_preview(request):
    posts = Post.objects.all()
    return render(request, 'blog_preview.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'post_detail.html', {'post': post})