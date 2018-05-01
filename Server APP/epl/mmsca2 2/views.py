# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Post


# Create your views here.
def index(request):
    return render(request, "home.html")


#create 

    

#Read
def getPost(request, id=1):
    #gets a post from db using id
    post = Post.objects.get(id=id)
    print(post.content)
    
    ctx = {"object" : post}
    return render(request, "post.html", ctx)

def getPosts(request):
    #gets a posts from db using id
    post = Post.objects.all()
    ctx = {"objects" : post}
    return render(request, "posts.html", ctx)
    
#update
    
#delete