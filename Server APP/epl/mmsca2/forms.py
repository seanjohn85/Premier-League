#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 22:04:34 2018

@author: johnkenny
"""

from django import forms

from .models import Post

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

