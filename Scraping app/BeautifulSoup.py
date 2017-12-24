#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:02:01 2017

@author: johnkenny


http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/
"""

from bs4 import BeautifulSoup

import requests

r  = requests.get("http://www.skysports.com/arsenal-results")

data = r.text

soup = BeautifulSoup(data)
#print(soup)

fixture = soup.findAll("div" ,{"class":"fixres matches-block--large"})

print(fixture)

for link in soup.find_all('h3'):
    print("New Month")
    print(link)
    
    
print("complete")
    

