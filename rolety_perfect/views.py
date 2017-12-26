# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rolety_perfect.models import *
from django.http import HttpResponse


def page(request):
    if request.path == "/" or request.path == "":
        model_url = "index.html"
    else:
        model_url = request.path.strip("/")
    page = Page.objects.get(url=model_url)
    content = Page.objects.get(url=model_url).post.content
    return render(request,
                  "rolety_perfect/{}.jj2".format(model_url),
                  {"page": page,
                   "content": content})
