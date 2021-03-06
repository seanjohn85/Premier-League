# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-01 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0012_auto_20180201_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeGoals', models.IntegerField(default=0)),
                ('awayGoals', models.IntegerField(default=0)),
                ('date', models.CharField(max_length=100)),
                ('awayTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awayTeam', to='rest.Team')),
                ('homeTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeTeam', to='rest.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='fixtures',
            name='awayTeam',
        ),
        migrations.RemoveField(
            model_name='fixtures',
            name='homeTeam',
        ),
        migrations.DeleteModel(
            name='Fixtures',
        ),
    ]
