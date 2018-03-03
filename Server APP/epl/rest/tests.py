# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


from .models import Team
from .models import Player
from .models import Fixture
from .models import Table


#test the team model
class TeamTestCase(TestCase):
    def setUp(self):
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
        import json
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
        
        