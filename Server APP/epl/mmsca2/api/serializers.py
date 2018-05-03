#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:58:40 2018

@author: johnkenny
"""

from django.contrib.auth import get_user_model

from rest_framework import serializers


from mmsca2.models import Post
from django.urls import reverse


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostModelSerializer(serializers.ModelSerializer):
    #read only so user details can not be manually added for posts
    user = UserSerializer(read_only=True)
    time = serializers.SerializerMethodField()
    view  = serializers.SerializerMethodField()
    update  = serializers.SerializerMethodField()
    delete  = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Post
        fields = ['id', 'user',"content", "time", "view", "update", "delete"]
        
    def get_time(self, obj):
        return obj.time.strftime("%b %d %y %I:%M %p")
    
    def get_view(self, obj):
        return reverse('getPost', kwargs={"pk" : obj.id})
    def get_update(self, obj):
        return reverse('update', kwargs={"pk" : obj.id})
    def get_delete(self, obj):
        return reverse('delete', kwargs={"pk" : obj.id})



