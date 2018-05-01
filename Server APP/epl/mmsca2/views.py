# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from dyango.urls import reverse_lazy


from .forms import PostModelForm
from .models import Post

from .mixins import FormUserRequiredMixin, OwnerMixin

# Create your views here.
def index(request):
    return render(request, "home.html")


#create 
class PostCreateView(FormUserRequiredMixin, CreateView):
    form_class = PostModelForm
    template_name = 'mmsca2/create.html'
    success_url = "home.html"


    
    
    
    
#Read
class PostDetailView(DetailView):
    queryset = Post.objects.all()
    





class PostListView(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Post.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        return context


#def getPost(request, pk=None):
#    #gets a post from db using id
#    post = Post.objects.get(pk=pk)
#    print(post.content)
#    
#    ctx = {"object" : post}
#    return render(request, "post.html", ctx)
#
#def getPosts(request):
#    #gets a posts from db using id
#    post = Post.objects.all()
#    ctx = {"objects" : post}
#    return render(request, "posts.html", ctx)
    
#update
        
class PostUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'mmsca2/update.html'
    success_url = "home.html"
    
#delete
    
class PostDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'mmsca2/delete.html'
    success_url = reverse_lazy("home.html")
    