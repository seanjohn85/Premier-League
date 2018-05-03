#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 22:04:34 2018

@author: johnkenny
"""

from django import forms

from .models import Post

from django.contrib.auth import get_user_model


User = get_user_model()


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
#        
#    def clean_content(self, *args, **kwargs):
#        content = self.cleaned_data.get("content")
#        if content == "liverpool":
#            raise forms.ValidationError("Cannot talk about this")
#        return content
        
        
        
class UserRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm =  forms.CharField(widget=forms.PasswordInput)
    
