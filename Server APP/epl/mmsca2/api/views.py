#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:58:10 2018

@author: johnkenny
"""

from rest_framework import generics
from mmsca2.models import Post
from django.db.models import Q
from rest_framework import permissions

from .serializers import PostModelSerializer


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    
    
    def get_queryset(self, *args, **kwargs):
        #order by newest post
        query = Post.objects.all().order_by("-time")
        print(self.request.GET)
        print(query)
        single = self.request.GET.get('q', None)
        if single is not None:
            
            query = query.filter(
                    Q(content__icontains=single) |
                    Q(user__username__icontains=single))
        return query
