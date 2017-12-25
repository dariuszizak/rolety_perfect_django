# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rolety_perfect.models import *


def index(request):
    page = Page.objects.get(url="index.html")
    content = Page.objects.get(url="index.html").post.content
    return render(request,
                  "rolety_perfect/index.html.jj2",
                  {"page": page,
                   "content": content})


def verticale(request):
    page = Page.objects.get(url="verticale.html")
    content = Page.objects.get(url="verticale.html").post.content
    return render(request,
                  "rolety_perfect/verticale.html.jj2",
                  {"page": page,
                   "content": content})


def zaluzje(request):
    page = Page.objects.get(url="zaluzje.html")
    content = Page.objects.get(url="zaluzje.html").post.content
    return render(request,
                  "rolety_perfect/zaluzje.html.jj2",
                  {"page": page,
                   "content": content})


def rolety_materialowe(request):
    page = Page.objects.get(url="rolety-materialowe.html")
    content = Page.objects.get(url="rolety-materialowe.html").post.content
    return render(request,
                  "rolety_perfect/rolety-materialowe.html.jj2",
                  {"page": page,
                   "content": content})


def rolety_zewnetrzne(request):
    page = Page.objects.get(url="rolety-zewnetrzne.html")
    content = Page.objects.get(url="rolety-zewnetrzne.html").post.content
    return render(request,
                  "rolety_perfect/rolety-zewnetrzne.html.jj2",
                  {"page": page,
                   "content": content})


def moskitiery(request):
    page = Page.objects.get(url="moskitiery.html")
    content = Page.objects.get(url="moskitiery.html").post.content
    return render(request,
                  "rolety_perfect/moskitiery.html.jj2",
                  {"page": page,
                   "content": content})


def kontakt(request):
    page = Page.objects.get(url="kontakt.html")
    content = Page.objects.get(url="kontakt.html").post.content
    return render(request,
                  "rolety_perfect/kontakt.html.jj2",
                  {"page": page,
                   "content": content})
