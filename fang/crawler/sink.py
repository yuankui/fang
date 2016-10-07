from house.models import OldHouse


class MysqlSink:
    def sink(self, data):
        data = self.flat(data)

        fields = OldHouse._meta.fields
        house = OldHouse()

        for field in fields:
            setattr(house, field.attname, data[field.attname])

        house.save()

    def flat(self, data):
        flatData = {}
        for k, v in data.items():
            if isinstance(v, dict):
                flatData.update(v)
            else:
                flatData[k] = v

        return flatData
