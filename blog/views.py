from django.shortcuts import render
from .models import Post
from django.utils import timezone

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    pass

def podcast(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/podcast.html', {'posts': posts})

def gallery(request):
    pass

def orderform(request):
    pass

def contact(request):
    pass
