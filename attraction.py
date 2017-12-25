#coding=utf-8
import requests
from bs4 import BeautifulSoup

class SpiderMain(object):
 def Crawl(self):
  class attraction:
     name = ""
     point=""
  response = requests.get("http://www.cncn.com/paihang/")
  soup = BeautifulSoup(response.text, "html.parser")
  attractions = []
  for day in soup.findAll(class_='child-noborder'):
     i = day.findAll("li")
     n = 0
     b = attraction()
     for div in i:
         if n==0:
             b.name = div.a.string
             b.point=div.em.string
         elif n == 1:
             b.name = div.a.string
             b.point = div.em.string
         elif n == 2:
             b.name = div.a.string
             b.point = div.em.string
         elif n == 3:
             n = 0
             attractions.append(b)
             break
         n += 1
     return attractions

