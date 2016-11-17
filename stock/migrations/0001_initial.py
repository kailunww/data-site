# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dividend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField()),
                ('money', models.DecimalField(decimal_places=4, max_digits=14)),
                ('price', models.DecimalField(decimal_places=4, max_digits=14)),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MoneyIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField()),
                ('money', models.DecimalField(decimal_places=4, max_digits=14)),
                ('price', models.DecimalField(decimal_places=4, max_digits=14)),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StockCode',
            fields=[
                ('code', models.SlugField(primary_key=True, serialize=False)),
                ('name_chi', models.CharField(max_length=100)),
                ('name_eng', models.CharField(max_length=100)),
                ('lot_size', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField()),
                ('project', models.PositiveSmallIntegerField(choices=[(1, 'IPO'), (2, 'LONG'), (3, 'SHORT')])),
                ('money', models.DecimalField(decimal_places=4, max_digits=14)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=4, max_digits=14)),
                ('broker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Broker')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.StockCode')),
            ],
        ),
        migrations.AddField(
            model_name='moneyin',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.StockIn'),
        ),
        migrations.AddField(
            model_name='dividend',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.StockIn'),
        ),
    ]