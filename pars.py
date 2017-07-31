# -*- coding: utf-8 -*-
from config import *
from bottle import route, run
from bs4 import BeautifulSoup
import urllib.request
import lxml, sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-l', '--link', default='', nargs='?')
    parser.add_argument ('-i', '--host', default='', nargs='?')
    parser.add_argument ('-p', '--port', default='', nargs='?')
    parser.add_argument ('-d', '--debug', default='', nargs='?')
    parser.add_argument ('-m', '--max_news', default='', nargs='?')
 
    return parser
 
parser = createParser()
namespace = parser.parse_args()

if namespace.link:     LINK = str(namespace.link)
if namespace.host:     HOST = str(namespace.host)
if namespace.port:     PORT = int(namespace.port)
if namespace.debug:    DEBUG = int(namespace.debug)
if namespace.max_news: MAX_NEWS = int(namespace.max_news)

news = {}
class News:
     def __init__(self, link):
        global news
        self.get_news_1_level(LINK)
     def get_news_1_level(self, link):
        self.link = link
        if DEBUG: print(self.link)
        self.req = urllib.request.Request(self.link, headers={'User-Agent': 'Mozilla/5.0'})
        self.url = urllib.request.urlopen(self.req).read()
        self.soup =  BeautifulSoup(self.url, "html.parser")
        self.body = self.soup.find_all('tr', {"class":"athing"})
        for tr in self.body:
            if (len(news) > (MAX_NEWS - 1)): break
            self.userId = tr.get("id")
            self.td = tr.find_all('td')
            self.userTitle = self.td[2].a.text
            self.userUrl = self.td[2].a.get("href")
            if self.td[2].span: self.userSite = self.td[2].span.a.text
            else: continue
            self.dic = dict(url=self.userUrl, title=self.userTitle, site=self.userSite)
            if self.userId in news.keys(): continue
            news[self.userId] = self.dic
        self.body = self.soup.find_all('td', {"class":"subtext"})	
        for td in self.body:
            if (len(news) > (MAX_NEWS - 1)): break
            self.author = td.a.text
            self.span = td.find_all('span', {"class":"age"})
            self.id = str(self.span).split('?id=')[1].split('">')[0]
            if DEBUG: print(self.id)
            news[self.id] = dict(url=self.userUrl, title=self.userTitle, site=self.userSite)
            news[self.id].update(author=self.author)
        return news

     def get_news_2_level(self):
        self.body = self.soup.find_all('span', {"class":"sitebit comhead"})
        for span in self.body:
           href = span.a.get("href")
           if DEBUG: print(href)
           if DEBUG: print("---------------sitebit comhead---------------")
           full_link = LINK + "/" + href
           if DEBUG: print(full_link)
           self.get_news_1_level(full_link)
           self.link = full_link
           self.re = urllib.request.Request(self.link, headers={'User-Agent': 'Mozilla/5.0'})
           self.ur = urllib.request.urlopen(self.re).read()
           self.sou =  BeautifulSoup(self.ur, "html.parser")
           self.bod = self.sou.find_all('a', {"class":"morelink"})
           if self.bod: 
               morelink = self.bod[0].get("href")
               full_morelink = LINK + "/" + morelink
               if DEBUG: print(full_morelink)
               self.get_news_1_level(full_morelink)	   
           else: 
               if DEBUG: print("not morelink")
           if (len(news) > (MAX_NEWS - 1)): break
		   
		   
		   
