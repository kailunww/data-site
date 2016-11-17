from django.db import models

# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=100)


class StockCode(models.Model):
    class Meta:
        ordering = ['code']

    code = models.SlugField(primary_key=True)
    name_chi = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    lot_size = models.PositiveIntegerField(default=0)


class Project:
    IPO = 1
    LONG = 2
    SHORT = 3


class StockIn(models.Model):
    project_choices = [
        (Project.IPO, "IPO"),
        (Project.LONG, "LONG"),
        (Project.SHORT, "SHORT"),

    ]
    code = models.ForeignKey(StockCode)
    add_date = models.DateField()
    broker = models.ForeignKey(Broker)
    project = models.PositiveSmallIntegerField(choices=project_choices)
    money = models.DecimalField(max_length=14, max_digits=4)
    price = models.DecimalField(max_length=14, max_digits=4)
    quantity = models.PositiveSmallIntegerField()
    parent = models.ForeignKey("StockIn")


class MoneyIn(models.Model):
    stock = models.ForeignKey(StockIn)
    add_date = models.DateField()
    money = models.DecimalField(max_length=14, max_digits=4)
    price = models.DecimalField(max_length=14, max_digits=4)
    quantity = models.PositiveSmallIntegerField()


class Dividend(models.Model):
    stock = models.ForeignKey(StockIn)
    add_date = models.DateField()
    money = models.DecimalField(max_length=14, max_digits=4)
    price = models.DecimalField(max_length=14, max_digits=4)
    quantity = models.PositiveSmallIntegerField()














