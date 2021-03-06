#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 15:08:26 2018

@author: johnkenny
"""

from django.http import HttpResponse
#class object repersenting db tables
from .models import Team
from .models import Player
from .models import Fixture
from .models import Table

 #used for json handling
import json
        
#extracting from web sources
import urllib

#class used to get data from the server
class GetData(object):
    def __init__(self):
      
        #api to get all data from fantasy football in json
        self.hres = urllib.urlopen('https://fantasy.premierleague.com/drf/bootstrap-static')
        #reads the json from the url
        self.data = json.loads(self.hres.read().decode("utf-8"))
        
        
    #function to get the league table and update the db   no longer used
    def getTable(self):
        #clear the previous state of the table in db
        Table.objects.all().delete()
        #request data from server
        import urllib2
        req = urllib2.Request("https://heisenbug-premier-league-live-scores-v1.p.mashape.com/api/premierleague/table", None, {"X-Mashape-Key": "Jqt3JPn10XmshB7WnEfMWs8KWKvZp1DeV2fjsnT9J7lJSXS0aw","Accept": "application/json"})
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
    
    #function to get the teams and undate the db        
    def getTeams(self):
        #loops through all teams crating or updating the database
        for team in self.data['teams']:
# =============================================================================
#             used for testing only
#             print(team['id'])
#             print(team['code'])
#             print(team['name'])
#             print(team['strength_defence_home'])
#             print(team['strength_attack_home'])
#             print(team['strength_overall_home'])
#             print(team['strength_attack_away'])
#             print(team['strength_defence_away'])
#             print(team['strength_overall_away'])
# =============================================================================
            #checks if the team already excits on the db
            queryset = Team.objects.filter(code = team['code'])
            #if the team doesnt excist create it on the db
            if not queryset:
                Team.objects.create(code = team['code'], name = team['name'], fixId = team['id'],
                                    strength_defence_home = team['strength_defence_home'],
                                    strength_attack_home = team['strength_attack_home'],
                                    strength_overall_home = team['strength_overall_home'],
                                    strength_attack_away =team['strength_attack_away'],
                                    strength_defence_away = team['strength_defence_away'],
                                    strength_overall_away = team['strength_overall_away'])
            else:
                #if it does excist update it
                queryset.update(fixId = team['id'], strength_defence_home = team['strength_defence_home'],
                                strength_attack_home = team['strength_attack_home'],
                                strength_overall_home = team['strength_overall_home'],
                                strength_attack_away =team['strength_attack_away'],
                                strength_defence_away = team['strength_defence_away'],
                                strength_overall_away = team['strength_overall_away'])
        
    def getPlayers(self):
        #loop through all the players from json file      
        for player in self.data['elements']:
            #find the players team
            qs = Team.objects.filter(code = player["team_code"])
            #ensure only one team is returned
            if qs.count() == 1:
                #store the team
                for t in qs:
                    team =  t
                #search bd to see if player already stored
                queryset = Player.objects.filter(playerId = player["id"])
                #set the squad numbers set to 0 if they have no current squad no to avoid db errors
                no = player["squad_number"]
                if no is None:
                    no = 0
                #if the player doesnt excist on the db create the player object and add to the db    
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
                    #if the player excits update it
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
    #function that deletes previous round of fixtures from the db and updates with the next round of fixtures and their predictions
    def getFixtures(self):
      #deletes previous fixtures
      Fixture.objects.all().delete()  
      #import the prediction class            
      from Prediction import Predictor
      #create a predictor object
      pd = Predictor()
      #loop through all the fixtures
      for fixture in self.data['next_event_fixtures']:
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
            #uses the predictor class to generate goals for each side
            hg = pd.goalGenerator(home.strength_attack_home - away.strength_defence_away)
            ag = pd.goalGenerator(away.strength_attack_away - home.strength_defence_home)
            #create fiture object
            Fixture.objects.create(homeTeam = home, awayTeam = away,homeGoals = hg, awayGoals = ag, date = fixture["kickoff_time_formatted"])
    
    #populates the league table using data from sky sports        
    def getTableSky(self):
         #clear the previous state of the table in db
        Table.objects.all().delete()
        from bs4 import BeautifulSoup
        import requests
        #link on skys website
        sky  = requests.get("http://www.skysports.com/premier-league-table")
        #converts the hml to text
        skyData = sky.text
        #feeds the downloaded data into beautiful soup library
        soup = BeautifulSoup(skyData, "html5lib")
        #gets all the rows of the league table fromthe html
        table=soup.findAll("tr" ,{"class":"standing-table__row"})
        #loops thgrough the rows 
        for row in table:
            #skip the header row
            data = row.find_all("th")
            if data:
                print("nonw")
            else:
                print("here")
        
                #team name
                print(row.select_one("td a:nth-of-type(1)").text)
                #played
                print(row.select_one("td:nth-of-type(3)").text)
                #won
                print(row.select_one("td:nth-of-type(4)").text)
                #drew
                print(row.select_one("td:nth-of-type(5)").text)
                #lost
                print(row.select_one("td:nth-of-type(6)").text)
                #gd
                print(row.select_one("td:nth-of-type(9)").text)
                #gd
                print(row.select_one("td:nth-of-type(10)").text)
                #create table object and update db
                Table.objects.create(team  = row.select_one("td a:nth-of-type(1)").text,
                   played      = row.select_one("td:nth-of-type(3)").text,
                   win         = row.select_one("td:nth-of-type(4)").text,
                   draw        = row.select_one("td:nth-of-type(5)").text,
                   loss        = row.select_one("td:nth-of-type(6)").text,
                   gd          = row.select_one("td:nth-of-type(9)").text,
                   points      = row.select_one("td:nth-of-type(10)").text)
                
                
                
def main():
    print('getting data')
    #the constructor downloads the json data from the pl api
    update = GetData()
    #updates all the teams data
    update.getTeams()
    #updates all the player date in db using the json 
    update.getPlayers()
    #changes to the next round of fixtures and makes a prediction(see the prediction class)
    update.getFixtures()
    #update table
    update.getTableSky()
    print('no error')

if __name__ == '__main__': main()
    


