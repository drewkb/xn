from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/list.html'
    context_object_name = 'latest_posts'
    
    def get_queryset(self):
        return Post.objects.order_by('-date')[:10]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


