# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-18 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20200218_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='added_by',
        ),
    ]
