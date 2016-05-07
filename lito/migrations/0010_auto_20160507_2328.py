# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-07 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lito', '0009_auto_20160507_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypoint',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='storypoint',
            name='soundcloud_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='storypoint',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
