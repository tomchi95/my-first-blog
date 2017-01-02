# -*- coding: utf-8 -*-
from datetime import datetime

import factory
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.test.client import Client
from factory.fuzzy import FuzzyText, FuzzyNaiveDateTime

from .models import Post


class PostFactory(factory.DjangoModelFactory):

    class Meta:
        model = Post
    title = FuzzyText(length=10, prefix='title_')
    slug = factory.LazyAttribute(lambda a: slugify(a.title))
    pub_date = FuzzyNaiveDateTime(datetime(2015, 3, 19))


class TestPost(TestCase):

    """testy dla aplikacji posts"""

    def setUp(self):
        self.client = Client()
        self.obj = PostFactory.create(title='test')

    def test_post_creation(self):
        NOW = datetime.now()
        obj = PostFactory.build(title='test', pub_date=NOW)
        self.assertTrue(isinstance(obj, Post))
        self.assertEqual(obj.__unicode__(), '%s z dnia %s' %
                         (obj.title, obj.pub_date))

    def test_post_list_response(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200, 'strona niedostępna')

    def test_post_detail_response(self):
        response = self.client.get(reverse('post-detail',
                                           kwargs={'slug': 'test'}))
        self.assertEqual(response.status_code, 200, 'strona niedostępna')
