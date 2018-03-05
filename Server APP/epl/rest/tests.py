# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


from .models import Team
from .models import Player
from .models import Fixture
from .models import Table

#used to add sample teams to db
def createTeams():
    Team.objects.create(code = 0, name = "Real Madrid", fixId = 0,
                                    strength_defence_home = 99,
                                    strength_attack_home = 99,
                                    strength_overall_home = 99,
                                    strength_attack_away = 99,
                                    strength_defence_away = 99,
                                    strength_overall_away = 99)
    Team.objects.create(code = 999, name = "PSG", fixId = 999,
                                    strength_defence_home = 99,
                                    strength_attack_home = 99,
                                    strength_overall_home = 99,
                                    strength_attack_away = 99,
                                    strength_defence_away = 99,
                                    strength_overall_away = 99)

#test the team model
class TeamTestCase(TestCase):
    def setUp(self):
        #creats sample teams
        createTeams()
        

    def testName(self):
        #gets the team code
        rm = Team.objects.get(code=0)
        psg = Team.objects.get(code= 999)
        self.assertEqual(rm.myName(), 'Real Madrid')
        self.assertEqual(psg.myName(), 'PSG')

        
    def testCode(self):
        #gets the team code
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        self.assertEqual(rm.code, 0)
        self.assertEqual(psg.code, 999)
        
    def test_strength_defence_home(self):
        #gets the strength_defence_home
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        self.assertEqual(rm.strength_defence_home, 99)
        self.assertEqual(psg.strength_defence_home, 99)
        
        
    def test_strength_attack_home(self):
        #gets the strength_attack_home
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        self.assertEqual(rm.strength_attack_home, 99)
        self.assertEqual(psg.strength_attack_home, 99)
        
    def test_strength_overall_home(self):
        #gets the strength_overall_home
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        self.assertEqual(rm.strength_attack_home, 99)
        self.assertEqual(psg.strength_attack_home, 99)
        
    def test_strength_attack_away(self):
        #gets the strength_attack_away
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        self.assertEqual(rm.strength_attack_away, 99)
        self.assertEqual(psg.strength_attack_away, 99)
        
        
    def test_strength_defence_away(self):
        #gets the strength_defence_away
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        self.assertEqual(rm.strength_defence_away, 99)
        self.assertEqual(psg.strength_defence_away, 99)
        
    def test_strength_overall_away(self):
        #gets the strength_overall_away
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        self.assertEqual(rm.strength_overall_away, 99)
        self.assertEqual(psg.strength_overall_away, 99)
        
        
        
    def test_json(self):
        rm = Team.objects.get(name="Real Madrid")
        psg = Team.objects.get(name="PSG")
        data = { 'name': "Real Madrid",
            'code': 0,
            'strength_defence_home'     : 99,
            'strength_attack_home'      : 99,
            'strength_overall_home'     : 99,
            'strength_attack_away'      : 99,
            'strength_defence_away'     : 99,
            'strength_overall_away'     : 99
        }
        self.assertEqual(rm.json(), data)
        data = { 'name': "PSG",
            'code': 999,
            'strength_defence_home'     : 99,
            'strength_attack_home'      : 99,
            'strength_overall_home'     : 99,
            'strength_attack_away'      : 99,
            'strength_defence_away'     : 99,
            'strength_overall_away'     : 99
        }
        self.assertEqual(psg.json(), data)
        
        
        
#test the Fixture model
class FixtureTestCase(TestCase):
    def setUp(self):
        #add sample teams
        createTeams()
        #add sample fixtures
        Fixture.objects.create(homeTeam    = Team.objects.get(name="Real Madrid"),
            awayTeam    = Team.objects.get(name="PSG"),
            homeGoals   = 1,
            awayGoals   = 2,
            date        = "10 Feb 2018"
                )
        Fixture.objects.create(homeTeam    = Team.objects.get(name="PSG"),
            awayTeam    = Team.objects.get(name="Real Madrid"),
            homeGoals   = 2,
            awayGoals   = 2,
            date        = "5 March 2018"
                )
        
    def testDate(self):
        #test the date
        rm = Fixture.objects.get(homeTeam = Team.objects.get(name="Real Madrid"))
        psg = Fixture.objects.get(homeTeam = Team.objects.get(name="PSG"))
        self.assertEqual(rm.date, "10 Feb 2018")
        self.assertEqual(psg.date, "5 March 2018")
        
    def testHomeGoals(self):
        #test the home goals
        rm = Fixture.objects.get(homeTeam = Team.objects.get(name="Real Madrid"))
        psg = Fixture.objects.get(homeTeam = Team.objects.get(name="PSG"))
        self.assertEqual(rm.homeGoals, 1)
        self.assertEqual(psg.homeGoals, 2)
        
    def testAwayGoals(self):
        #test the away goals
        rm = Fixture.objects.get(homeTeam = Team.objects.get(name="Real Madrid"))
        psg = Fixture.objects.get(homeTeam = Team.objects.get(name="PSG"))
        self.assertEqual(rm.awayGoals, 2)
        self.assertEqual(psg.awayGoals, 2)
        
    def testAwayTeam(self):
        #test the away team
        rm = Fixture.objects.get(homeTeam = Team.objects.get(name="Real Madrid"))
        psg = Fixture.objects.get(homeTeam = Team.objects.get(name="PSG"))
        self.assertEqual(rm.awayTeam, Team.objects.get(name="PSG"))
        self.assertEqual(psg.awayTeam, Team.objects.get(name="Real Madrid"))
        
    def testHomeTeam(self):
        #test the home team
        rm = Fixture.objects.get(awayTeam = Team.objects.get(name="Real Madrid"))
        psg = Fixture.objects.get(awayTeam = Team.objects.get(name="PSG"))
        self.assertEqual(rm.homeTeam, Team.objects.get(name="PSG"))
        self.assertEqual(psg.homeTeam, Team.objects.get(name="Real Madrid"))
        
    def test_Json(self):
        #test json
        rm = Fixture.objects.get(homeTeam = Team.objects.get(name="Real Madrid"))
        psg = Fixture.objects.get(homeTeam = Team.objects.get(name="PSG"))
        data = {
              'homeTeam'          : Team.objects.get(name="Real Madrid").name,
              'awayTeam'          : Team.objects.get(name="PSG").name,
              'homeGoals'         : 1,
              'awayGoals'         : 2,
              'date'              : "10 Feb 2018",
          }
        self.assertEqual(rm.json(), data)
        data = {
              'homeTeam'          : Team.objects.get(name="PSG").name,
              'awayTeam'          : Team.objects.get(name="Real Madrid").name,
              'homeGoals'         : 2,
              'awayGoals'         : 2,
              'date'              : "5 March 2018",
          }
        self.assertEqual(psg.json(), data)
        
        
#test the Table model
class TableTestCase(TestCase):
    def setUp(self):
        #add sample fixtures
        Table.objects.create(team = "Real Madrid", played = 5, win = 3, draw = 1,loss = 1, gd = 12, points = 10)
        Table.objects.create(team = "PSG", played = 5, win = 4, draw = 1, loss = 0, gd = 17, points = 13)

    def testPlayed(self):
        #test the played matches
        rm = Table.objects.get(team = "Real Madrid")
        psg = Table.objects.get(team = "PSG")
        self.assertEqual(rm.played, 5)
        self.assertEqual(psg.played, 5)
        
    def testTeams(self):
        #test the teams by won matches
        rm = Table.objects.get(win = 3)
        psg = Table.objects.get(win = 4)
        self.assertEqual(rm.team, "Real Madrid")
        self.assertEqual(psg.team, "PSG")
        
    def testWin(self):
        #test the won
        rm = Table.objects.get(team = "Real Madrid")
        psg = Table.objects.get(team = "PSG")
        self.assertEqual(rm.win, 3)
        self.assertEqual(psg.win, 4)
        
    def testLoss(self):
        #test the loss
        rm = Table.objects.get(team = "Real Madrid")
        psg = Table.objects.get(team = "PSG")
        self.assertEqual(rm.loss, 1)
        self.assertEqual(psg.loss, 0)
        
    def testDraw(self):
        #test the played matches
        rm = Table.objects.get(team = "Real Madrid")
        psg = Table.objects.get(team = "PSG")
        self.assertEqual(rm.draw, 1)
        self.assertEqual(psg.draw, 1)
    
    def testgd(self):
        #test the goal difference
        rm = Table.objects.get(team = "Real Madrid")
        psg = Table.objects.get(team = "PSG")
        self.assertEqual(rm.gd, 12)
        self.assertEqual(psg.gd, 17)
    
    def testPoints(self):
        #test the points
        rm = Table.objects.get(team = "Real Madrid")
        psg = Table.objects.get(team = "PSG")
        self.assertEqual(rm.points, 10)
        self.assertEqual(psg.points, 13)
        
    def test_Json(self):
        #test json
        rm = Table.objects.get(team = "Real Madrid")
        psg = Table.objects.get(team = "PSG")
        data = {
              'team'              : "Real Madrid",
              'played'            : 5,
              'win'               : 3,
              'draw'              : 1,
              'loss'              : 1,
              'gd'                : 12,
              'points'            : 10
          
          }
        self.assertEqual(rm.json(), data)
        data = {
              'team'              : "PSG",
              'played'            : 5,
              'win'               : 4,
              'draw'              : 1,
              'loss'              : 0,
              'gd'                : 17,
              'points'            : 13
          
          }
        self.assertEqual(psg.json(), data)
        
        
        
#test the Player model
class PlayerTestCase(TestCase):
    def setUp(self):
        #add sample teams
        createTeams()
        #add sample fixtures
        Player.objects.create(playerId = 7777,
            #each player has one team
            teams               = Team.objects.get(name="Real Madrid"),
            f_name              = "Gareth",
            l_name              = "Bale",
            pos                 = 3,
            goals               = 20,
            assits              = 5,
            photo               = "gb.png")
        
        Player.objects.create(playerId = 7778,
            #each player has one team
            teams               = Team.objects.get(name="PSG"),
            f_name              = "Angle",
            l_name              = "Di Maria",
            pos                 = 3,
            goals               = 6,
            assits              = 7,
            photo               = "dim.png")
   
        
        
    def testName(self):
        #test the players names
        rm = Player.objects.get(teams = Team.objects.get(name="Real Madrid"))
        psg = Player.objects.get(teams = Team.objects.get(name="PSG"))
        self.assertEqual(rm.f_name, "Gareth")
        self.assertEqual(rm.l_name, "Bale")
        self.assertEqual(psg.f_name, "Angle")
        self.assertEqual(psg.l_name, "Di Maria")
        
        
    def testTeam(self):
        #test the teams
        rm = Player.objects.get(l_name = "Bale")
        psg = Player.objects.get(l_name = "Di Maria")
        self.assertEqual(rm.teams, Team.objects.get(name="Real Madrid"))
        self.assertEqual(psg.teams,Team.objects.get(name="PSG"))
        
        
    def testPos(self):
        #test the teams
        rm = Player.objects.get(l_name = "Bale")
        psg = Player.objects.get(l_name = "Di Maria")
        self.assertEqual(rm.pos, 3)
        self.assertEqual(psg.pos, 3)
        
    def testGoals(self):
        #test the teams
        rm = Player.objects.get(l_name = "Bale")
        psg = Player.objects.get(l_name = "Di Maria")
        self.assertEqual(rm.goals, 20)
        self.assertEqual(psg.goals, 6)
        
    def testAssits(self):
        #test the teams
        rm = Player.objects.get(l_name = "Bale")
        psg = Player.objects.get(l_name = "Di Maria")
        self.assertEqual(rm.assits, 5)
        self.assertEqual(psg.assits, 7)
        
    def testPhoto(self):
        #test the teams
        rm = Player.objects.get(l_name = "Bale")
        psg = Player.objects.get(l_name = "Di Maria")
        self.assertEqual(rm.photo, "gb.png")
        self.assertEqual(psg.photo, "dim.png")
        
    def testJson(self):
        #test the teams
        rm = Player.objects.get(l_name = "Bale")
        psg = Player.objects.get(l_name = "Di Maria")
        data = {
            'playerId'          : 7777,
            'teams'             : Team.objects.get(name="Real Madrid").code,
            'f_name'            : "Gareth",
            'l_name'            : "Bale",
            'pos'               : 3,
            'goals'             : 20,
            'assits'            : 5,
            'saves'             : 0,
            'clean_sheets'      : 0,
            'number'            : 0,
            'goals_conceded'    : 0,
            'own_goals'         : 0,
            'penalties_saved'   : 0,
            'photo'             : "gb.png",
            'penalties_missed'  : 0,
            'yellow_cards'      : 0,
            'red_cards'         : 0,
            'news'              : None, 
        }
        self.assertEqual(rm.json(), data)
        data = {
            'playerId'          : 7778,
            'teams'             : Team.objects.get(name="PSG").code,
            'f_name'            : "Angle",
            'l_name'            : "Di Maria",
            'pos'               : 3,
            'goals'             : 6,
            'assits'            : 7,
            'saves'             : 0,
            'clean_sheets'      : 0,
            'number'            : 0,
            'goals_conceded'    : 0,
            'own_goals'         : 0,
            'penalties_saved'   : 0,
            'photo'             : "dim.png",
            'penalties_missed'  : 0,
            'yellow_cards'      : 0,
            'red_cards'         : 0,
            'news'              : None, 
        }
        self.assertEqual(psg.json(), data)
        
        
#        
##test the predictor class
#from Prediction import Predictor
#
#class PredicyionTestCase(TestCase):
#
#    def setUp(self):
#        #add sample teams
#        createTeams()
#    def testPrediction(self):
#        #create a predictor object
#       pd = Predictor()
#       goals= pd.goalGenerator(67)
#       self.assertTrue(goals.is_float())
        
        
  
    
        