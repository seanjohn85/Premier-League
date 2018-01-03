# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from .models import Team
from .models import Player


#used for json handling
import json

#extracting from web sources
import urllib


def index(request):
    queryset = Team.objects.filter(code = 8888888)
    #if the query is empty
    if not queryset:
        return HttpResponse("error")
    else:
        str = ""
        for team in queryset:
            str = str + team.json()
        return HttpResponse(str)
    
    
#method to update palyer and team opjects on the db. this is currently called by a url but will be moved to a timed interval
def create_UpdateDB(request):
    #opens the url
    #api to get all data from fantasy football in json
    hres = urllib.urlopen('https://fantasy.premierleague.com/drf/bootstrap-static')
    #reads the json from the url
    data = json.loads(hres.read().decode("utf-8"))
    #loops through all teams crating or updating the database
    for team in data['teams']:
        print(team['code'])
        print(team['name'])
        print(team['strength_defence_home'])
        print(team['strength_attack_home'])
        print(team['strength_overall_home'])
        print(team['strength_attack_away'])
        print(team['strength_defence_away'])
        print(team['strength_overall_away'])
        queryset = Team.objects.filter(code = team['code'])
        if not queryset:
            Team.objects.create(code = team['code'], name = team['name'], 
                                strength_defence_home = team['strength_defence_home'],
                                strength_attack_home = team['strength_attack_home'],
                                strength_overall_home = team['strength_overall_home'],
                                strength_attack_away =team['strength_attack_away'],
                                strength_defence_away = team['strength_defence_away'],
                                strength_overall_away = team['strength_overall_away'])
        else:
            queryset.update(strength_defence_home = team['strength_defence_home'],
                            strength_attack_home = team['strength_attack_home'],
                            strength_overall_home = team['strength_overall_home'],
                            strength_attack_away =team['strength_attack_away'],
                            strength_defence_away = team['strength_defence_away'],
                            strength_overall_away = team['strength_overall_away'])
            
            
    for player in data['elements']:
        qs = Team.objects.filter(code = player["team_code"])
        #print(qs)
        if qs.count() == 1:
            for t in qs:
                team =  t
                print("team found")
            queryset = Player.objects.filter(playerId = player["id"])
            no = player["squad_number"]
            if no is None:
                no = 0
            if not queryset:
                Player.objects.create(playerId = player["id"], teams = team,
                                      f_name = player["first_name"], l_name =player["second_name"],
                                      pos = player["element_type"], goals = player["goals_scored"],
                                      assits = player["assists"], saves = player["saves"], 
                                      clean_sheets = player["clean_sheets"], number = no,
                                      goals_conceded = player["goals_conceded"], own_goals = player["own_goals"],
                                      penalties_saved = player["penalties_saved"], photo = player["photo"].replace(".jpg", ""),
                                      penalties_missed = player["penalties_missed"], yellow_cards = player["yellow_cards"],
                                      red_cards = player["red_cards"], influence = player["influence"],
                                      creativity = player["creativity"], threat = player["threat"],
                                      news = player["news"]
                        )
            else:
                queryset.update(teams = team,
                                      pos = player["element_type"], goals = player["goals_scored"],
                                      assits = player["assists"], saves = player["saves"], 
                                      clean_sheets = player["clean_sheets"], number = no,
                                      goals_conceded = player["goals_conceded"], own_goals = player["own_goals"],
                                      penalties_saved = player["penalties_saved"],
                                      penalties_missed = player["penalties_missed"], yellow_cards = player["yellow_cards"],
                                      red_cards = player["red_cards"], influence = player["influence"],
                                      creativity = player["creativity"], threat = player["threat"],
                                      news = player["news"]
                        )


    return HttpResponse("complete")
            


def testPage(request):
    return render(request, base.html, context)


def teams(request):
    return HttpResponse("Hello, world2. You're at the rest api test.")

#from rest_framework import viewsets
#from rest_framework import permissions
#from .serializers import TeamSerializer
#
## Create your views here.
class TeamViewSet():
    print("here")
    
    










