# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldhouse',
            name='age',
        ),
        migrations.RemoveField(
            model_name='oldhouse',
            name='name',
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='community',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='decoration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='direction',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='houseId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='size',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='totalFloor',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='withLift',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oldhouse',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
