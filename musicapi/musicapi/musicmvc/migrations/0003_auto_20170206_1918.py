# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicmvc', '0002_auto_20170206_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
