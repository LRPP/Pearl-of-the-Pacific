from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    pass

def about(request):
    pass

def podcast(request):
    pass

def gallery(request):
    pass

def orderform(request):
    pass

def contact(request):
    pass
