# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-30 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lito', '0003_auto_20160405_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='storypoint',
            name='created_date',
        ),
    ]