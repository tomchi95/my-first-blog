# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.published()


class PostDetailView(DetailView):
    model = Post
