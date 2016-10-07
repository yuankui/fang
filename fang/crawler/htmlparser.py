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
        self.format(data)
        return data

    def format(self, data):
        size = data['houseInfo']['size']
        size = self.NUM_REGEX.findall(size)[0]
        data['houseInfo']['size'] = float(size)

        price = data['price']
        price = self.NUM_REGEX.findall(price)[0]
        data['price'] = float(price)

    def parse_house_info(self, houseInfo):
        text = houseInfo.get_text()
        values = text.split(r'|')
        fields = ['community', '_', 'size', 'direction', 'decoration', 'with_lift']
        data = dict(zip(fields, values))
        return data

    POSITION_REG = re.compile(r'.楼层\(共(.+)层\)\s+((\d+)年.+  )?-  (.+)')

    def parse_position_info(self, positionInfo):
        try:
            text = positionInfo.get_text()

            match = self.POSITION_REG.match(text)
            fields = ['totalFloor', '_', 'year', 'position']
            values = match.groups()
            return dict(zip(fields, values))
        except Exception as e:
            logging.error("parse_position_info:%s", str(positionInfo), e)
