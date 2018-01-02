#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:01:21 2017

@author: johnkenny
"""

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]  