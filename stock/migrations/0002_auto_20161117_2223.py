# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockin',
            name='project',
            field=models.CharField(choices=[('IPO', 'IPO'), ('LONG', 'LONG'), ('SHORT', 'SHORT')], max_length=10),
        ),
    ]
