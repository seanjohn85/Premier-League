# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-31 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=80)),
                ('l_name', models.CharField(max_length=80)),
                ('pos', models.CharField(max_length=20)),
                ('goals', models.IntegerField(default=0)),
                ('assits', models.IntegerField(default=0)),
                ('saves', models.IntegerField(default=0)),
                ('clean_sheets', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('goals_conceded', models.IntegerField(default=0)),
                ('own_goals', models.IntegerField(default=0)),
                ('penalties_saved', models.IntegerField(default=0)),
                ('photo', models.CharField(max_length=100)),
                ('penalties_missed', models.IntegerField(default=0)),
                ('yellow_cards', models.IntegerField(default=0)),
                ('red_cards', models.IntegerField(default=0)),
                ('influence', models.IntegerField(default=0)),
                ('creativity', models.IntegerField(default=0)),
                ('threat', models.IntegerField(default=0)),
                ('news', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('strength_defence_home', models.IntegerField(default=0)),
                ('strength_attack_home', models.IntegerField(default=0)),
                ('strength_overall_home', models.IntegerField(default=0)),
                ('strength_attack_away', models.IntegerField(default=0)),
                ('strength_defence_away', models.IntegerField(default=0)),
                ('strength_overall_away', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='teams',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footballdata.Team'),
        ),
    ]