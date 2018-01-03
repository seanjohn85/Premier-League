#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:01:21 2017

@author: johnkenny
"""

from django.conf.urls import url

from . import views

#from rest_framework import routers


urlpatterns = [
        url(r'^hello', views.hello_world, name="hello_world"),
    # Examples:
    # url(r'^$', 'marine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^team/', views.create_UpdateDB, name='create_UpdateDB'),
    url(r'^squad/', views.squad, name='squad'),
]  