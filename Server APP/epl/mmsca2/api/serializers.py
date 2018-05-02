#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:58:40 2018

@author: johnkenny
"""

from django.contrib.auth import get_user_model

from rest_framework import serializers


from mmsca2.models import Post


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostModelSerializer(serializers.ModelSerializer):
    #read only so user details can not be manually added for posts
    user = UserSerializer(read_only=True)
    time = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['user',"content", "time"]
        
    def get_time(self, obj):
        return obj.time.strftime("%b %d %y %I:%M %p")


