from django.shortcuts import render
from .models import Post
from django.utils import timezone

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def podcast(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/podcast.html', {'posts': posts})

def episode(request):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/episode.html', {'post': post})

def gallery(request):
    return render(request, 'blog/gallery.html')

def orderform(request):
    return render(request, 'blog/orderform.html')

def contact(request):
    return render(request, 'blog/contact.html')
