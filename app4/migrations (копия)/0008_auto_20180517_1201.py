# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-17 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0007_auto_20180516_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='result',
        ),
        migrations.AddField(
            model_name='person',
            name='result1',
            field=models.IntegerField(default=0),
        ),
    ]
