#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:01:21 2017

@author: johnkenny
"""

from django.conf.urls import url

from . import views

from django.views.generic import TemplateView

from rest.views import teams

from rest.views import testPage

urlpatterns = [
    url(r'^$', views.index, name='index'),
]  