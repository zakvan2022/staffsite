# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffapp', '0006_auto_20170923_0332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='end_job',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='start_job',
            new_name='start_time',
        ),
    ]
