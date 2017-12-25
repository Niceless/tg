#coding=utf-8
import requests
from bs4 import BeautifulSoup

import bmob as utils

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
             data={'name':b.name,'point':b.point}
             resp=utils.insert(table_name='Attraction',data=data)
         elif n == 1:
             b.name = div.a.string
             b.point = div.em.string
             data = {'name': b.name, 'point': b.point}
             resp = utils.insert(table_name='Attraction', data=data)
         elif n == 2:
             b.name = div.a.string
             b.point = div.em.string
             data = {'name': b.name, 'point': b.point}
             resp = utils.insert(table_name='Attraction', data=data)
         elif n == 3:
             n = 0
             attractions.append(b)
             break
         n += 1

