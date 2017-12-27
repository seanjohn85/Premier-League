#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:38:54 2017

@author: johnkenny
"""

#used for file io
import os, errno

#used for json handling
import json

#extracting from web sources
import urllib
    
#function takes url and stores images from url
def savePlayerImages():
    #opens the url
    #api to get all data from fantasy football in json
    hres = urllib.urlopen('https://fantasy.premierleague.com/drf/bootstrap-static')
    #reads the json from the url
    data = json.loads(hres.read().decode("utf-8"))
    #gets all the team objects
    for team in data['teams']:
        print(team['name'])
        print(team['code'])
        t1 = Team(team['name'], str(team['code']))
        t1.createdir()
    
    #gets all the player objetcs
    for player in data['elements']:
        name = player["first_name"] + "_" + player["second_name"]
        print(player["photo"].replace(".jpg", ""))
        photo = player["photo"].replace(".jpg", "")
        p1 = Player(str(player["team_code"]), name, photo) 
        p1.savePhoto()
    return


class Player(object):
    #used for player objects to save images
    
    #constructor
    def __init__(self, team, name, photo):
        self.team = team
        self.name = name 
        self.photo = photo
        self.url = "https://platform-static-files.s3.amazonaws.com/premierleague/photos/players/250x250/p" + self.photo + ".png"
        self.fileLoc = team + "/" + photo + ".png"
        
    def savePhoto(self):
        #used to save photos 
        # sample url  https://platform-static-files.s3.amazonaws.com/premierleague/photos/players/250x250/p169743.png
        urllib.urlretrieve(self.url, self.fileLoc)
        

class Team(object):
    #used for team objects
    
    def __init__(self, name, code):
        self.name = name
        self .code = code
        
    def createdir(self):
        print("here")
        try:
            os.makedirs(self.code)
            print("directory created for " + self.name + " called " + self.code)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


        
savePlayerImages()
        
       
        
        
    
    