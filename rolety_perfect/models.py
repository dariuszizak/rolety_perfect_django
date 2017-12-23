# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from froala_editor.fields import FroalaField


class Page(models.Model):
    """
    Model for identifing page name. Server as king of page ID.
    """
    page_url = models.CharField(max_length=30)
    page_title = models.CharField(max_length=100)
    canonical_link = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)

    def __unicode__(self):
        return self.page_url


class Post(models.Model):
    """
    Model for storing post which constists of headings below h1, paragraph and
    photos.
    """
    page_url = models.ForeignKey(Page,
                                 on_delete=models.CASCADE)
    content = FroalaField()

    def __unicode__(self):
        return self.title
