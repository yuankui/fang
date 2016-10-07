import logging

import requests
import bs4
from . import htmlparser
from . import sink


def run():
    area_config = [
        ('xihu', '西湖区'),
        ('xiacheng', '下城区'),
        ('jianggan', '江干区'),
        ('gongshu', '拱墅区'),
        ('shangcheng', '上城区'),
        ('binjiang', '滨江'),
        ('yuhang', '余杭区'),
        ('xiaoshan', '萧山区'),
    ]

    for area in area_config:
        for page in range(1, 120):

            url = 'http://hz.lianjia.com/ershoufang/%s/pg%d/' % (area[0], page)

            content = requests.get(url).content

            bs = bs4.BeautifulSoup(content, 'html5lib')

            s = bs.select('ul.listContent li.clear')

            print('getting:', len(s), url)
            output = sink.MysqlSink()
            for item in s:
                data = htmlparser.LianjiaParser().parse(item)
                data['area'] = area[1]
                output.sink(data)
