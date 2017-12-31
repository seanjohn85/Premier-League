#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:19:37 2017

@author: johnkenny

Team Class

"""

class Team(object):
    
    def __init__(self, code, name, strength_defence_home, strength_attack_home, strength_overall_home, 
                 strength_attack_away, strength_defence_away, strength_overall_away):
        
        self.code = code
        self.name = name
        self.strength_defence_home = strength_defence_home
        self.strength_attack_home = strength_attack_home
        self.strength_overall_home = strength_overall_home
        self.strength_attack_away = strength_attack_away
        self.strength_defence_away = strength_defence_away
        self.strength_overall_away = strength_overall_away