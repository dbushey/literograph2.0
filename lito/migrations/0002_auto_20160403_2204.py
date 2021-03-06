# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypoint',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='storypoint',
            name='longitute',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitute',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
