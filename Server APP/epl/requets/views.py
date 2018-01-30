# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import json

def test(request):
    return HttpResponse("This is a test")



def index(request):
    data = {
        'name': 'Paul Pogba',
        'Team': 'Manchester United',
        'Number': 6,
        'age': 24
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


