#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:15:20 2017

@author: johnkenny

from FOLDER_NAME import FILENAME
from FILENAME import CLASS_NAME FUNCTION_NAME
"""



from Player import Player
p1 = Player("", "", "", "", "", "", "", "", "", "", "",
                 "", "", "", "", "", "", "",
                 "", "")

#used for json handling
import json

#extracting from web sources
import urllib

#function to get players position test block
def postion(code):
    if code == 1:
        return "Goalkeeper"
    elif code == 2:
        return "Defender"
    elif code == 3:
        return "Midfielder"
    elif code == 4:
        return "Striker"
    
print(postion(3))


from Team import Team

t1 = Team("", "", "", "", "", 
                 "", "", "")