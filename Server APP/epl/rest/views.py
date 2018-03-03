# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
import urllib2

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
    #this object downloads info from the net on players ans teams please view its class for more infor
    from GetData import GetData
    #the constructor downloads the json data from the pl api
    update = GetData()
    #updates all the teams data
    update.getTeams()
    #updates all the player date in db using the json 
    update.getPlayers()
    #changes to the next round of fixtures and makes a prediction(see the prediction class)
    update.getFixtures()
# =============================================================================
     
#     update.getTable()
#     update.getTeams()
#     update.getPlayers()
# =============================================================================
    
    return HttpResponse("updated data")






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
                #gets league table data
                tableQy = Table.objects.all()
                for row in tableQy:
                    print ("row")
                    table.append(row.json())
                    
            return Response({"team": club, "players" : players, "qty": qty, "fixture" : fixture, "table" :table})




        
        
        








