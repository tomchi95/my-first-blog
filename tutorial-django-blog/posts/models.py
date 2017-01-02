# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class PostManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(active=True,
                                          pub_date__lt=datetime.today())


class Post(models.Model):
    active = models.BooleanField(verbose_name=u'aktywny',
                                 default=False)
    pub_date = models.DateTimeField(verbose_name=u'data publikacji',
                                    null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name=u'tytuł')
    slug = models.SlugField()
    lead = models.TextField(verbose_name=u'wprowadzenie')
    body = models.TextField(verbose_name=u'treść posta')
    author = models.ForeignKey(User, verbose_name=u'autor',
                               null=True, blank=True)

    objects = PostManager()

    def __unicode__(self):
        return u"%s z dnia %s" % (self.title, self.pub_date)

    class Meta:
        verbose_name = u'wpis'
        verbose_name_plural = u'wpisy'
