# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-01 22:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0008_auto_20180201_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nextgame',
            name='awayTeam',
        ),
        migrations.RemoveField(
            model_name='nextgame',
            name='homeTeam',
        ),
        migrations.DeleteModel(
            name='nextGame',
        ),
    ]
