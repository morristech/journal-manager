# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20170217_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='version',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
