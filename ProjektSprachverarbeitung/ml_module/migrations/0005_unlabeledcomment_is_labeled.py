# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-09-06 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_module', '0004_remove_staging_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='unlabeledcomment',
            name='is_labeled',
            field=models.BooleanField(default=False),
        ),
    ]