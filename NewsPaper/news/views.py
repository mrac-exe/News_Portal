from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = ('date_post')
    template_name = 'news.html'
    context_object_name = 'news'

class PostDetail(DetailView):
    model = Post
    template_name = 'paper.html'
    context_object_name = 'paper'
