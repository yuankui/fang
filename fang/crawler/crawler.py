import logging

import requests
import bs4
from . import htmlparser
from . import sink


def run():

    for page in range(1, 120):

        url = 'http://hz.lianjia.com/ershoufang/pg%d/' % (page,)
        print('getting:', url)
        content = requests.get(url).content

        bs = bs4.BeautifulSoup(content, 'html5lib')

        s = bs.select('ul.listContent li.clear')

        output = sink.MysqlSink()
        for item in s:
            data = htmlparser.LianjiaParser().parse(item)
            output.sink(data)
