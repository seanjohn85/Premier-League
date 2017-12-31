#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:46:15 2017

@author: johnkenny

Player class used to create player objects

"""

#used to create players
class Player(object):
    
    #constructer to match the pl json api lib attritubes
    def __init__(self, dbid, f_name, l_name, team, pos, goals, assits, saves, clean_sheets, number, goals_conceded,
                 own_goals, penalties_saved, photo, penalties_missed, yellow_cards, red_cards, influence,
                 creativity, threat, news):
        self.dbid = dbid
        self.f_name = f_name
        self.l_name = l_name
        self.team = team
        self.pos = pos
        self.goals = goals
        self.assits = assits
        self.saves = saves
        self.clean_sheets = clean_sheets
        self.number = number
        self.goals_conceded = goals_conceded
        self.own_goals = own_goals
        self.penalties_saved = penalties_saved
        self.photo = photo
        self.penalties_missed = penalties_missed
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.influence = influence
        self.creativity = creativity
        self.threat = threat
        self.news = news
        
        
        
    #function to get players position
# =============================================================================
#     def postion(code):
#         if code == 1:
#             return "Goalkeeper"
#         elif code == 2:
#             return "Defender"
#         elif code == 3:
#             return "Midfielder"
#         elif code == 4:
#             return "Striker"
# =============================================================================
        
    def dbCheck():
        #if statement to check if this object excists on the db and creates or updates
        return


p1 = Player("", "", "", "", "", "", "", "", "", "", "",
                 "", "", "", "", "", "", "",
                 "", "", "")