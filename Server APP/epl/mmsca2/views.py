# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
User = get_user_model()


from .forms import PostModelForm, UserRegisterForm
from .models import Post

from .mixins import FormUserRequiredMixin, OwnerMixin

# Create your views here.
def index(request):
    return render(request, "home.html")


class UserRegisterView(FormView):
    template_name = 'mmsca2/signup.html'
    form_class = UserRegisterForm
 
    success_url = "/mmsca2/posts/"
    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)
    


#create 
class PostCreateView(FormUserRequiredMixin, CreateView):
    form_class = PostModelForm
    template_name = 'mmsca2/create.html'
   #success_url = reverse_lazy("index")


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs = User.objects.filter(
                    Q(username__icontains=query)
                )
        context = {"users": qs}
        return render(request, "mmsca2/post_list.html", context)    
    
    
    
#Read
class PostDetailView(DetailView):
    queryset = Post.objects.all()
    





class PostListView(ListView):
    queryset = Post.objects.all()
    
    def get_queryset(self, *args, **kwargs):
        query = Post.objects.all()
        print(self.request.GET)
        print(query)
        single = self.request.GET.get('q', None)
        if single is not None:
            
            query = query.filter(
                    Q(content__icontains=single) |
                    Q(user__username__icontains=single))
        return query
        

    def get_context_data(self, *args, **kwargs):
        ctx = super(PostListView, self).get_context_data(*args, **kwargs)
        ctx['create_form'] = PostModelForm()
        ctx['action_url'] = reverse_lazy("create")
        return ctx


#update
        
class PostUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'mmsca2/update.html'
    #success_url = reverse_lazy("index")
    
#delete
    
class PostDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'mmsca2/delete.html'
    success_url = reverse_lazy("getPosts2")
    