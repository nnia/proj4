# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0004_auto_20180516_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
