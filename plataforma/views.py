from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'home.html', context)


def listar_post(request, id):
    posts = Post.objects.get(pk=id)
    context = {
        'posts':posts 
    }

    return render(request, 'listar_post.html', context)

