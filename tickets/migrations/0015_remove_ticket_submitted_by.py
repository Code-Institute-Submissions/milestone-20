# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-18 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0014_ticket_submitted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='submitted_by',
        ),
    ]
