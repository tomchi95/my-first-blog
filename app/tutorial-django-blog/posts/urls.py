# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
]
