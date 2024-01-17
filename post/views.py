from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    tags = Tag.objects.all()

    search_query = request.GET.get('q', '')
    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(tag__name__icontains=search_query))

    return render(request, 'post_list.html', {'posts': posts, 'tags': tags, 'search_query': search_query})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    tags = Tag.objects.all()

    return render(request, 'post_detail.html', {'post': post, 'tags': tags})

def blog_index(request):
    try:
        special_post = Post.objects.get(is_index_post=True)
    except Post.DoesNotExist:
        special_post = None
    context = {'special_post': special_post}
    return render(request, 'blog_index.html', context)