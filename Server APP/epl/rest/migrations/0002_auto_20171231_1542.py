# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-31 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AlterField(
            model_name='player',
            name='playerId',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
