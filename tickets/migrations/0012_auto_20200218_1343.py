# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-18 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20200218_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='submitted_by',
            new_name='added_by',
        ),
    ]
