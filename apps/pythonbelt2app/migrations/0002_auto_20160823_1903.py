# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonbelt2app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='Pending', max_length=15),
        ),
    ]
