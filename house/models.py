from django.db import models


# Create your models here.

class OldHouse(models.Model):
    name = models.TextField()
    age = models.IntegerField()