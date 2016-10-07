import requests
import bs4
from . import htmlparser
from . import sink


def run():
    content = requests.get('http://hz.lianjia.com/ershoufang/p2/').content

    bs = bs4.BeautifulSoup(content, 'html5lib')

    s = bs.select('ul.listContent li.clear')

    output = sink.MysqlSink()
    for item in s:
        data = htmlparser.LianjiaParser().parse(item)
        output.sink(data)
