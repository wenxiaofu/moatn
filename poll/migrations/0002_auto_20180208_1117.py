# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-08 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private',
            name='begin_time',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='private',
            name='end_time',
            field=models.CharField(default='', max_length=200),
        ),
    ]
