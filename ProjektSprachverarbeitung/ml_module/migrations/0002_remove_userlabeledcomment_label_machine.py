# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-08-14 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlabeledcomment',
            name='label_machine',
        ),
    ]
