# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False, verbose_name='aktywny')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='data publikacji', blank=True)),
                ('title', models.CharField(max_length=25, verbose_name='tytu\u0142')),
                ('slug', models.SlugField()),
                ('lead', models.TextField(verbose_name='wprowadzenie')),
                ('body', models.TextField(verbose_name='tre\u015b\u0107 posta')),
                ('author', models.ForeignKey(verbose_name='autor', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'wpis',
                'verbose_name_plural': 'wpisy',
            },
        ),
    ]
