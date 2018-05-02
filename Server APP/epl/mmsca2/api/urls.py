#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:01:21 2017

@author: johnkenny
"""

from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from . import views
from .views import PostListAPIView, PostCreateAPIView

#from rest_framework import routers


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='getPosts'),
    url(r'^create/', PostCreateAPIView.as_view(), name='create'), 
    # Examples:
    # url(r'^$', 'marine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^$', views.index, name='index'),
#    url(r'^posts/', PostListView.as_view(), name='getPosts'), 
#    url(r'^create/', PostCreateView.as_view(), name='create'), 
#    url(r'^(?P<pk>\d+)/update/', PostUpdateView.as_view(), name='update'),
#    url(r'^(?P<pk>\d+)/delete/', PostDeleteView.as_view(), name='delete'),
#    url(r'^(?P<pk>\d+)/', PostDetailView.as_view(), name='getPost'), 
    

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)