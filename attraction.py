#coding=utf-8
import requests
from bs4 import BeautifulSoup

class SpiderMain(object):
 def Crawl(self,url):
     hot_url=url
     if url is None:
         return None
     response = requests.get(hot_url)
     soup = BeautifulSoup(response.text, "html.parser")
     attraction = []
     for day in soup.findAll(class_='child-noborder'):
         i = day.findAll("li")
         n = 0
         for div in i:
             attractions = {}
             attractions['name'] = div.a.string
             attraction.append(attractions)
             #attractions['point'] = div.em.int
             #print div.em.string
         return attraction



