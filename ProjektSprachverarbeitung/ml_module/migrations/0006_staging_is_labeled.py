# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-09-06 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_module', '0005_unlabeledcomment_is_labeled'),
    ]

    operations = [
        migrations.AddField(
            model_name='staging',
            name='is_labeled',
            field=models.BooleanField(default=False),
        ),
    ]
