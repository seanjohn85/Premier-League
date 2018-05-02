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
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ['user',"content"]


