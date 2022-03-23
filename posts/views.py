from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse


def index(request):
    form = PostForm(request.POST, request.FILES)
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    # if the form is valid
        if form.is_valid():

            # yes,save
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')

        else:

            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html', {'posts': posts, 'form': form})


def delete(request, post_id):

    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        print("hello world")
        form = PostForm(request.POST, request.FILES, instance=post)
    # if the form is valid
        if form.is_valid():

            # yes,save
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')

        else:

            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())
    return render(request, 'edit.html', {'post': post})


def like(request, post_id):

    newlikecount = Post.objects.get(id=post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')
