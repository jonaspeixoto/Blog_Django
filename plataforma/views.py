from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'home.html', context)


