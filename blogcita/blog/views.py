from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context={
        'Title':'HEY ASSHOLES',
        'Content':"HEYOOOOO",
        'Posts':posts,
    }
    return render(request, 'blog/index.html',context)

def detailPost(request, slug):
    post = Post.objects.get(slug=slug)
    context={
        'Title':'HEY',
        'Content':"HEYOOOOO",
        'Posts':post,
    }
    return render(request, '/blog/detail.html', context)