# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rl_app', '0002_auto_20180131_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(max_length=5, verbose_name='性别'),
        ),
    ]
