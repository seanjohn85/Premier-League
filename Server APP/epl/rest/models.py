# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

#Class used to create team objects and team table structure in db
class Team(models.Model):
    code                    = models.IntegerField(primary_key=True,  unique=True)
    name                    = models.CharField(max_length=80)
    fixId                   = models.IntegerField(default=0)
    strength_defence_home   = models.IntegerField(default=0)
    strength_attack_home    = models.IntegerField(default=0)
    strength_overall_home   = models.IntegerField(default=0)
    strength_attack_away    = models.IntegerField(default=0)
    strength_defence_away   = models.IntegerField(default=0)
    strength_overall_away   = models.IntegerField(default=0)
  
    
    def returnMe(self):
        return self
    #used to return a json object containing a team
    def json(self):

        data = {
            'name': self.name,
            'code': self.code,
            'strength_defence_home'     : self.strength_defence_home,
            'strength_attack_home'      : self.strength_attack_home,
            'strength_overall_home'     : self.strength_overall_home,
            'strength_attack_away'      : self.strength_attack_away,
            'strength_defence_away'     : self.strength_defence_away,
            'strength_overall_away'     : self.strength_overall_away
            
        }
        dump = json.dumps(data)
        return data

    
    
#Class used to create Player objects and player table structure in db
class Player(models.Model):
    playerId            = models.IntegerField(primary_key=True, unique=True)
    #each player has one team
    teams               = models.ForeignKey(Team, on_delete=models.CASCADE)
    f_name              = models.CharField(max_length=80)
    l_name              = models.CharField(max_length=80)
    pos                 = models.IntegerField(default=0)
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
    influence           = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    creativity          = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    threat              = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    news                = models.CharField(max_length=500, blank=True, null=True)
    #used to return a json player object
    def json(self):

        data = {
            'playerId'          : self.playerId,
            'teams'             : self.teams.code,
            'f_name'            : self.f_name,
            'l_name'            : self.l_name,
            'pos'               : self.pos,
            'goals'             : self.goals,
            'assits'            : self.assits,
            'saves'             : self.saves,
            'clean_sheets'      : self.clean_sheets,
            'number'            : self.number,
            'goals_conceded'    : self.goals_conceded,
            'own_goals'         : self.own_goals,
            'penalties_saved'   : self.penalties_saved,
            'photo'             : self.photo,
            'penalties_missed'  : self.penalties_missed,
            'yellow_cards'      : self.yellow_cards,
            'red_cards'         : self.red_cards,
#            'influence'         : "" + self.influence,
#            'creativity'        : "" +self.creativity,
#            'threat'            : "" +self.threat,
            'news'              : self.news
            
        }
        dump = json.dumps(data)
        return data


#next fixture table
class Fixture(models.Model):
    #one to one relationship established with 2 teams for each fixture
    homeTeam    = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='homeTeam')
    awayTeam    = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='awayTeam')
    homeGoals   = models.IntegerField(default=0)
    awayGoals   = models.IntegerField(default=0)
    date        = models.CharField(max_length=100)
    #returns the fixure data in json format
    def json(self):
        data = {
             'homeTeam'           : self.homeTeam.name,
              'awayTeam'          : self.awayTeam.name,
              'homeGoals'         : self.homeGoals,
              'awayGoals'         : self.awayGoals,
              'date'              : self.date,
          
          }
        dump = json.dumps(data)
        return data





