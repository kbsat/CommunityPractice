from django.shortcuts import render, redirect
from .models import Post

# Create your views here.


def main(request):
    posts = Post.objects.all
    return render(request, 'main.html', {'posts': posts})


def post(request):
    return render(request, 'post.html')


def new(request):
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']

    post.save()
    return redirect('/')
