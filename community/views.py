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


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'update.html', {'post': post})


def update_save(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    new_title = request.GET['title']
    new_content = request.GET['content']
    if post.title != new_title or post.content != new_content:
        post.title = new_title
        post.content = new_content
        post.save()

    return redirect('/detail/'+str(post_id))


def new(request):
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']

    post.save()
    return redirect('/')
