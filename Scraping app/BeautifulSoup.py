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

fixture=soup.findAll("div" ,{"class":"fixres__body"})

#print(fixture)
#
#for f in fixture:
#    print("start")
#    print(f.find("h4").get_text())
#    print("end")
#        #latest.append(news.noscript.img.attrs.get('src'))
#        #latest.append(news.find("div",{"class":"news-list__body"}).p.get_text())
#        #itemdetail=news.find("div",{"class":"news-list__body"})
#        #latest.append(itemdetail.p.get_text())
#        #latest.append(re.sub('\s+',' ',itemdetail.h4.get_text()))
#        #latest.append(itemdetail.h4.a.attrs.get('href'))
#        #item={"imgsrc":news.noscript.img.attrs.get('src'),"title":re.sub('\s+',' ',itemdetail.h4.get_text()),"shortdesc":itemdetail.p.get_text(),"link":itemdetail.h4.a.attrs.get('href')}
#        #latest.append(item)
#    #return latest

for link in soup.find_all("h4",{"class":"fixres__header2"}):
    print("New Month")
    print(link.get_text())
    

for link in soup.find_all('h3'):
    print("New Month")
    print(link)
    

print("complete")
    

