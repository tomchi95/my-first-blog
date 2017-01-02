# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'active', )
    list_filter = ('active', 'author', )
    date_hierarchy = 'pub_date'
    search_fields = ('title', )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

admin.site.site_header = u'Mój blog'
