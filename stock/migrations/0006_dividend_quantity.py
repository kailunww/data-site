# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_remove_dividend_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='dividend',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]