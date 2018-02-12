#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 03:47:56 2018

@author: johnkenny

class used to make match predictions using a lamba fuction aand poison dist
"""

#class object repersenting db tables
from .models import Team

#used to create match predictions
class Predictor(object):
    
    def __init__(self):
        teams = Team.objects.all()
        self.maxAtt = 0
        self.minAtt = 0
        self.minGoals = 0.32
        self.maxGoals = 2.65
        for t in teams:
        
            for t2 in teams:
                #check if the teams are the same team and skip if so
                if t2.name != t.name:
                   
                    if t.strength_attack_home - t2.strength_defence_away > self.maxAtt:
                        self.maxAtt = t.strength_attack_home - t2.strength_defence_away
                    elif t.strength_attack_home - t2.strength_defence_away < self.minAtt: 
                        self.minAtt = t.strength_attack_home - t2.strength_defence_away
                   
                    if t2.strength_attack_away - t.strength_defence_home > self.maxAtt:
                       self. maxAtt = t2.strength_attack_away - t.strength_defence_home
                    elif t2.strength_attack_away - t.strength_defence_home < self.minAtt: 
                         self.minAtt = t2.strength_attack_away - t.strength_defence_home
        print(self.minAtt)
        print(self.maxAtt)
    
    
    def getExpectedGoals(self, compare):
        print(self.minGoals + (self.maxGoals - self.minGoals) * (compare - self.minAtt) / (self.maxAtt - self.minAtt))
        return self.minGoals + (self.maxGoals - self.minGoals) * (compare - self.minAtt) / (self.maxAtt - self.minAtt)
    
    def goalGenerator(self, compare):
        import numpy
        goals = numpy.random.poisson(self.getExpectedGoals(compare))
        print("x is ", goals)
        return goals