# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-07 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='serial_no',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]