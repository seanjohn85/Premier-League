# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Team
from .models import Player

from .models import Fixture
from .models import Table

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Fixture)
admin.site.register(Table)
