# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20170105_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('content', models.BinaryField()),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.Journal'),
        ),
    ]
