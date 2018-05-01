#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:50:58 2018

@author: johnkenny
"""
from django import forms
from django.forms.utils import ErrorList

class FormUserRequiredMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated(): 
            form.instance.user = self.request.user
            return super(FormUserRequiredMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User Must Be Logged In"])
            return self.form_invalid(form)
    
    
class OwnerMixin(FormUserRequiredMixin, object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormUserRequiredMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You can onlt edit your own posts"])
            return self.form_invalid(form)
    