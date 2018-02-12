# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0014_team_fixid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=80)),
                ('played', models.IntegerField(default=0)),
                ('win', models.IntegerField(default=0)),
                ('draw', models.IntegerField(default=0)),
                ('loss', models.IntegerField(default=0)),
                ('gd', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
    ]