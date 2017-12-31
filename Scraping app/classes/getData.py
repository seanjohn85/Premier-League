#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:56:01 2017

@author: johnkenny

get info from pl fansay

"""

#used for json handling
import json

#extracting from web sources
import urllib

def getPlayersData():
    #opens the url
    #api to get all data from fantasy football in json
    hres = urllib.urlopen('https://fantasy.premierleague.com/drf/bootstrap-static')
    #reads the json from the url
    data = json.loads(hres.read().decode("utf-8"))

    
    #gets all the player objetcs
    for player in data['elements']:
        print("")
        print(player["photo"])
        print(player["first_name"])
        print(player["second_name"])
        print(player["team_code"])
        print(player["id"])
        print(player["squad_number"])
        print(player["news"])
        print(player["squad_number"])
        print(player["influence"])
        print(player["creativity"])
        print(player["threat"])
        #position
        print(player["element_type"])
        print(player["penalties_saved"])
        print(player["penalties_missed"])
        print(player["yellow_cards"])
        print(player["red_cards"])
        print(player["saves"])
        print(player["goals_scored"])
        print(player["assists"])
        print(player["clean_sheets"])
        print(player["goals_conceded"])
        print(player["own_goals"])
        print(player["penalties_saved"])
        print(player["penalties_missed"])
        
    return
    

getPlayersData()

def getTeams():
    from Team import Team

    #opens the url
    #api to get all data from fantasy football in json
    hres = urllib.urlopen('https://fantasy.premierleague.com/drf/bootstrap-static')
    #reads the json from the url
    data = json.loads(hres.read().decode("utf-8"))
    #gets all the team objects
    for team in data['teams']:
        print(team['code'])
        print(team['name'])
        print(team['strength_defence_home'])
        print(team['strength_attack_home'])
        print(team['strength_overall_home'])
        print(team['strength_attack_away'])
        print(team['strength_defence_away'])
        print(team['strength_overall_away'])
        
        t1 = Team(team['code'], team['name'], team['strength_defence_home'], team['strength_attack_home'], 
                  team['strength_overall_home'], team['strength_attack_away'], team['strength_defence_away'], 
                  team['strength_overall_away'])
        
        
getTeams()

