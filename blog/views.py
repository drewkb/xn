from django.shortcuts import render
from .models import Post


def lst(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts':posts})
