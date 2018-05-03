#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:01:21 2017

@author: johnkenny
"""

from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserRegisterView, SearchView

#from rest_framework import routers


urlpatterns = [
        
    # Examples:
    # url(r'^$', 'marine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', PostListView.as_view(), name='index'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^register/', UserRegisterView.as_view(), name='register'),
    url(r'^posts/', PostListView.as_view(), name='getPosts'), 
    url(r'^posts/', PostListView.as_view(), name='getPosts2'),
    url(r'^create/', PostCreateView.as_view(), name='create'), 
    url(r'^(?P<pk>\d+)/update/', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/', PostDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/', PostDetailView.as_view(), name='getPost'), 
    

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)