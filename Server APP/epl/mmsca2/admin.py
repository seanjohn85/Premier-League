# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .forms import PostModelForm
from .models import Post

#admin.site.register(Post)

class PostModelAdmin(admin.ModelAdmin):
    class Meta:
       model = Post
        
        
admin.site.register(Post, PostModelAdmin)