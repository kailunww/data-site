# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20161121_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmaster',
            name='remark',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
