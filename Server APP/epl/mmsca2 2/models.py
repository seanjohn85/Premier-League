# -*- coding: utf-8 -*-
#allows the user admin framework be imported 
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    #content of the post
    content     = models.TextField(max_length=160)
    #time
    time        = models.DateTimeField(auto_now=True)
    update      = models.DateTimeField(auto_now_add=True)
    #user data using the user modle
    username    = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    #return a string of the content from the db
    def returnPost(self):
        return str(self.content)
    