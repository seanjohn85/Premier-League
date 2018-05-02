#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:58:10 2018

@author: johnkenny
"""

from rest_framework import generics
from mmsca2.models import Post

from .serializers import PostModelSerializer

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    
    
    def get_queryset(self):
        return Post.objects.all()
