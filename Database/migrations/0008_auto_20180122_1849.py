# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-22 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0007_auto_20180122_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.IntegerField(default=0),
        ),
    ]
