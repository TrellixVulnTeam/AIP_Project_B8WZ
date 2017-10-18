# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-18 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquor',
            name='can_or_bottle',
            field=models.CharField(default='bottle', max_length=150),
        ),
        migrations.AddField(
            model_name='liquor',
            name='category',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='liquor',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]