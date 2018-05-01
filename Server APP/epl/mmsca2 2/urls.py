#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:01:21 2017

@author: johnkenny
"""

from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

#from rest_framework import routers


urlpatterns = [
        
    # Examples:
    # url(r'^$', 'marine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^post/', views.getPost, name='getPost'),
    url(r'^posts', views.getPosts, name='getPosts'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)