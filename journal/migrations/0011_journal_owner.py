# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0010_auto_20170106_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]