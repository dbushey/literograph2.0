# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-01 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lito', '0004_auto_20160430_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
