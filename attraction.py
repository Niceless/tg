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
               attractions={}
               if n==0:
                   attractions['name']=div.a.string
                   attractions['point']=long(div.em.string)
                   attraction.append(attractions)
               elif n == 1:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 2:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 3:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 4:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 5:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 6:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 7:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 8:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 9:
                   attractions['name'] = div.a.string
                   attractions['point'] = long(div.em.string)
                   attraction.append(attractions)
               elif n == 10:
                    n = 0
                    break
               n += 1
        return attraction

