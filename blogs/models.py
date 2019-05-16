# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class blog(models.Model):
    id1 = models.AutoField(primary_key=True)
    user = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=20000)
    image = models.FileField()


class Comment(models.Model):
    id1 = models.ForeignKey(blog)
    comm = models.CharField(max_length=2000)
