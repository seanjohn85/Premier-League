# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

#class object repersenting db tables
from .models import Team
from .models import Player
from .models import Fixture
from .models import Table



#used for json handling
import json

#extracting from web sources
import urllib



# for testing teams
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
    
    
#test return players for a team
def squad(request):
    #man utd team hard coded
    teams = Team.objects.filter(code = 1)
    if not teams:
        return HttpResponse("error")
    else:
        str = ""
        
        for team in teams:
            str = str + team.json()
            playersQuery = Player.objects.filter(teams = team)
            for p in playersQuery:
                str = str + p.json()

    dump = json.dumps(str)
    return HttpResponse(dump, content_type='application/json')



#function to set the league table from the api - key limited to 25 trys per month
def getTable():
   #clear the previous state of the table in db
   Table.objects.all().delete()
   #request data from server
   import urllib2
   req = urllib2.Request("https://heisenbug-premier-league-live-scores-v1.p.mashape.com/api/premierleague/table?from=1", None, {"X-Mashape-Key": "cZbPUOwquimshoLXosqhuUAvn6lPp1QGfXTjsnHCziLoaVjfdI","Accept": "application/json"})
   response = urllib2.urlopen(req)
   #convert data to readable json
   data = json.loads(response.read().decode("utf-8"))
   #loop trough the records which is each teams table position
   for row in data['records']:
       gd = row['goalsFor'] - row['goalsAgainst']
       Table.objects.create(team  = row['team'],
           played      = row['played'],
           win         = row['win'],
           draw        = row['draw'],
           loss        = row['loss'],
           gd          = gd,
           points      = row['points'])

    
#method to update palyer and team opjects on the db. this is currently called by a url but will be moved to a timed interval
def create_UpdateDB(request):
    #getTable()
    #opens the url
    #api to get all data from fantasy football in json
    hres = urllib.urlopen('https://fantasy.premierleague.com/drf/bootstrap-static')
    #reads the json from the url
    data = json.loads(hres.read().decode("utf-8"))
    #deletes previous fixtures
    Fixture.objects.all().delete()
    #loops through all teams crating or updating the database
    for team in data['teams']:
        print(team['id'])
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
            Team.objects.create(code = team['code'], name = team['name'], fixId = team['id'],
                                strength_defence_home = team['strength_defence_home'],
                                strength_attack_home = team['strength_attack_home'],
                                strength_overall_home = team['strength_overall_home'],
                                strength_attack_away =team['strength_attack_away'],
                                strength_defence_away = team['strength_defence_away'],
                                strength_overall_away = team['strength_overall_away'])
        else:
            queryset.update(fixId = team['id'], strength_defence_home = team['strength_defence_home'],
                            strength_attack_home = team['strength_attack_home'],
                            strength_overall_home = team['strength_overall_home'],
                            strength_attack_away =team['strength_attack_away'],
                            strength_defence_away = team['strength_defence_away'],
                            strength_overall_away = team['strength_overall_away'])
            
    #loop through all the players from json file      
    for player in data['elements']:
        #find the players team
        qs = Team.objects.filter(code = player["team_code"])
        #ensure only one team is returned
        if qs.count() == 1:
            #store the team
            for t in qs:
                team =  t
                print("team found")
            #search bd to see if player already stored
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

    pd = Predictor()
    for fixture in data['next_event_fixtures']:
        
        print(fixture["team_a"])
        print(fixture["team_h"])
         #find the home team
        homeqs = Team.objects.filter(fixId = fixture["team_h"])
    
        for h in homeqs:
            home= h
            print(home.name)
            
            
         #find the away team
        awayqs = Team.objects.filter(fixId = fixture["team_a"])
        for a in awayqs:
            away = a
            print(away.name)
            
            away.strength_defence_away
            
        #create fiture object
        Fixture.objects.create(homeTeam = home, pd.goalGenerator(home.strength_attack_home - away.strength_defence_away), pd.goalGenerator(away.strength_attack_away - home.strength_defence_home), awayTeam = away, date = fixture["kickoff_time_formatted"])
        
    
    
    return HttpResponse("complete")






 #iOS rest api
from rest_framework.response import Response
from rest_framework.decorators import api_view

#test rest api call
@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Hello World!"})

    else:
        name = request.data.get("name")
        if not name:
            return Response({"error": "No name passed"})
        return Response({"message": "Hello {}!".format(name)})
    
#ios request used to get a teams data    
@api_view(["GET", "POST"])
def getData(request):
    #ensures the method is a post
    if request.method == "GET":
        return Response({"error": "No prams!"})
   #find the pram name 
    else:
        name = request.data.get("name")
        #if no name return an error message
        if not name:
            return Response({"error": "No team name passed"})
        queryset = Team.objects.filter(name = name)
        if not queryset:
            return Response({"error": "Team Name Invalid"})
        else:
            club = {}
            fixture = {}
            table = []
            #tableQuery = 
            for team in queryset:
                club = team.json()
                playersQuery = Player.objects.filter(teams = team)
                fix1 = Fixture.objects.filter(homeTeam = team) | Fixture.objects.filter(awayTeam = team)
                for f in fix1:
                    fixture = f.json()
                    print(f.json())
                players = []
                qty = 0
                for p in  playersQuery:
                    players.append(p.json())
                    qty = qty + 1
                    
                return Response({"team": club, "players" : players, "qty": qty, "fixture" : fixture})


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
        print("x is ", x)
        return goals
# =============================================================================
#         import math
#         import random
#         expectedGoals = -self.getExpectedGoals(compare)
#         goals = 0
#         limit = math.exp(expectedGoals)
#         ranNo = random.uniform(1, 10)
#         while ranNo > limit:
#             goals +=1
#             ranNo *= random.uniform(1, 10)
#             
#         print(goals)
#         return goals
# =============================================================================
        
        
        








