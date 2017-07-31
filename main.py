# -*- coding: utf-8 -*-

from pars import *
from api import *


a = News(LINK)
print(a.get_news_2_level())
print(str(len(news)) + " news were received")
if DEBUG: print(news)

run(host=HOST, port=PORT, debug=DEBUG)
