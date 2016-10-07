import logging
import re


class LianjiaParser():
    NUM_REGEX = re.compile(r'[0-9.]+')

    URL_REGEX = re.compile(r'(\d+).html')

    def parse(self, item):
        data = {}

        data['title'] = item.select('div.title')[0].get_text()
        data['price'] = item.select('div.totalPrice')[0].get_text()
        data['houseInfo'] = self.parse_house_info(item.select('div.houseInfo')[0])
        data['positionInfo'] = self.parse_position_info(item.select('div.positionInfo')[0])

        data['url'] = item.select('div.title')[0].a['href']
        data['id'] = self.URL_REGEX.findall(data['url'])[0]
        data['followInfo'] = self.parse_follow_info(item.select('div.followInfo')[0])
        self.format(data)
        return data

    def format(self, data):
        size = data['houseInfo']['size']
        size = self.NUM_REGEX.findall(size)[0]
        data['houseInfo']['size'] = float(size)

        price = data['price']
        price = self.NUM_REGEX.findall(price)[0]
        data['price'] = float(price)

        pos = data['positionInfo']
        pos['totalFloor'] = int(pos['totalFloor']) if pos['year'] is not None else None
        pos['year'] = int(pos['year']) if pos['year'] is not None else None


        follow = data['followInfo']
        follow['follow'] = int(follow['follow']) if follow['follow'] is not None else None
        follow['visit'] = int(follow['visit']) if follow['visit'] is not None else None

    def parse_house_info(self, houseInfo):
        text = houseInfo.get_text()
        values = text.split(r'|')
        fields = ['community', '_', 'size', 'direction', 'decoration', 'withLift']
        data = dict(zip(fields, values))
        return data

    POSITION_REG = re.compile(r'.楼层\(共(.+)层\)\s+(((\d+)年)?(.+))?\s*-\s+(.+)')

    def parse_position_info(self, positionInfo):
        try:
            text = positionInfo.get_text()

            match = self.POSITION_REG.match(text)
            fields = ['totalFloor', '_', '_', 'year', '_', 'position']
            values = match.groups()
            return dict(zip(fields, values))
        except Exception as e:
            logging.error("parse_position_info:%s", str(positionInfo), e)

    FOLLOW_REG = re.compile(r'(\d+)人关注 / 共(\d+)次带看 / (.+以前发布)')

    def parse_follow_info(self, followInfo):
        text = followInfo.get_text()

        match = self.FOLLOW_REG.match(text)
        fields = ['follow', 'visit', 'publishBefore']
        values = match.groups()
        return dict(zip(fields, values))