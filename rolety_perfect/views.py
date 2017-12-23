# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "rolety_perfect/index.html.jj2")


def verticale(request):
    return render(request, "rolety_perfect/verticale.html.jj2")


def zaluzje(request):
    return render(request, "rolety_perfect/zaluzje.html.jj2")


def rolety_materialowe(request):
    return render(request, "rolety_perfect/rolety-materialowe.html.jj2")


def rolety_zewnetrzne(request):
    return render(request, "rolety_perfect/rolety-zewnetrzne.html.jj2")


def moskitiery(request):
    return render(request, "rolety_perfect/moskitiery.html.jj2")


def kontakt(request):
    return render(request, "rolety_perfect/kontakt.html.jj2")
