# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    code                    = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name                    = models.CharField(max_length=80)
    number   = models.IntegerField(default=0)
