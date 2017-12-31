# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
    code                    = models.IntegerField(primary_key=True,  unique=True)
    name                    = models.CharField(max_length=80)
    strength_defence_home   = models.IntegerField(default=0)
    strength_attack_home    = models.IntegerField(default=0)
    strength_overall_home   = models.IntegerField(default=0)
    strength_attack_away    = models.IntegerField(default=0)
    strength_defence_away   = models.IntegerField(default=0)
    strength_overall_away   = models.IntegerField(default=0)
    
    
    
class Player(models.Model):
    playerId            = models.IntegerField(primary_key=True, unique=True)
    teams               = models.ForeignKey(Team, on_delete=models.CASCADE)
    f_name              = models.CharField(max_length=80)
    l_name              = models.CharField(max_length=80)
    pos                 = models.CharField(max_length=20)
    goals               = models.IntegerField(default=0)
    assits              = models.IntegerField(default=0)
    saves               = models.IntegerField(default=0)
    clean_sheets        = models.IntegerField(default=0)
    number              = models.IntegerField(default=0)
    goals_conceded      = models.IntegerField(default=0)
    own_goals           = models.IntegerField(default=0)
    penalties_saved     = models.IntegerField(default=0)
    photo               = models.CharField(max_length=100)
    penalties_missed    = models.IntegerField(default=0)
    yellow_cards        = models.IntegerField(default=0)
    red_cards           = models.IntegerField(default=0)
    influence           = models.IntegerField(default=0)
    creativity          = models.IntegerField(default=0)
    threat              = models.IntegerField(default=0)
    news                = models.CharField(max_length=500, blank=True, null=True)