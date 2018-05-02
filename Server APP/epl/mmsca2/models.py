# -*- coding: utf-8 -*-
#allows the user admin framework be imported 
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django.urls import reverse



def validate_content(value):
    if value == "":
        raise ValidationError("Cannot be blank")
    return value

# Create your models here.

class Post(models.Model):
    #content of the post
    content     = models.TextField(max_length=160, validators=[validate_content])
    #time
    time        = models.DateTimeField(auto_now=True)
    update      = models.DateTimeField(auto_now_add=True)
    #user data using the user modle
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    #return a string of the content from the db
    def returnPost(self):
        return str(self.content)
    
    def get_absolute_url(self):
        return reverse('getpost', kwargs={"pk" : self.pk})
    
    
    
   
    
    
#    def clean (self, *args, **kwargs):
#        content = self.content
#        
#        return super(Post, self).clean(*args, **kwargs)
#        
#    