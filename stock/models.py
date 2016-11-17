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

    def __str__(self):
        return "%s" % self.code


class Project:
    IPO = "IPO"
    LONG = "Long"
    SHORT = "Short"


class StockIn(models.Model):
    project_choices = [
        (Project.IPO, "IPO"),
        (Project.LONG, "Long"),
        (Project.SHORT, "Short"),

    ]
    add_date = models.DateField()
    code = models.ForeignKey(StockCode)
    project = models.CharField(max_length=10, choices=project_choices)
    money = models.DecimalField(max_digits=14, decimal_places=4)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=14, decimal_places=4)
    broker = models.ForeignKey(Broker, null=True, blank=True)


class MoneyIn(models.Model):
    stock = models.ForeignKey(StockIn)
    add_date = models.DateField()
    money = models.DecimalField(max_digits=14, decimal_places=4)
    price = models.DecimalField(max_digits=14, decimal_places=4)
    quantity = models.PositiveSmallIntegerField()


class Dividend(models.Model):
    stock = models.ForeignKey(StockIn)
    add_date = models.DateField()
    money = models.DecimalField(max_digits=14, decimal_places=4)
    price = models.DecimalField(max_digits=14, decimal_places=4)
    quantity = models.PositiveSmallIntegerField()














