from django.db import models


# Create your models here.

class OldHouse(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    community = models.CharField(max_length=100, null=True)
    decoration = models.CharField(max_length=100, null=True)
    direction = models.CharField(max_length=100,  null=True)
    size = models.FloatField(null=True)
    withLift = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    totalFloor = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
