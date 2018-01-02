# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Team


def index(request):
    queryset = Team.objects.filter(code = 8888888)
    str = ""
    for team in queryset:
        str = str + team.json()
    return HttpResponse(str)


def testPage(request):
    return render(request, base.html, context)


def teams(request):
    return HttpResponse("Hello, world2. You're at the rest api test.")



