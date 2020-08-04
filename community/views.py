from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.


def main(request):
    posts = Post.objects.all
    return render(request, 'main.html', {'posts': posts})


def post(request):
    return render(request, 'post.html')


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})


def new(request):
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']

    post.save()
    return redirect('/')
