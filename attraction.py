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
             if n == 0:
                attractions['name'] = div.a.string
                attractions['point'] = div.em.string
                print attractions['name']
             elif n == 1:
                 attractions['name'] = div.a.string
                 attractions['point'] = div.em.string
                 print attractions['name']
             elif n == 2:
                 attractions['name'] = div.a.string
                 attractions['point'] = div.em.string
                 print attractions['name']
             elif n==3:
                attraction.append(attractions)
                break
             n += 1

         return attraction


