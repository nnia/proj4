# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-17 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(default=0)),
                ('result', models.IntegerField(default=0)),
            ],
        ),
    ]