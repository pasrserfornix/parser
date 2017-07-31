# -*- coding: utf-8 -*-
from bottle import route, run
from config import *
from pars import *

@route('/api/posts/<name>')
def index(name):
    for i in news:
	    if news[i]['site'] == name: return str(news[i]) + "\n"

@route('/api/posts/')
def index():
    return news	