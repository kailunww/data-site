from django.db import models

# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.name


class StockCode(models.Model):
    class Meta:
        ordering = ['code']

    code = models.SlugField(primary_key=True)
    name_chi = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    lot_size = models.PositiveIntegerField(default=0)
    latest_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    last_update = models.DateTimeField(null=True)

    def __str__(self):
        return "%s" % self.code


class Project:
    IPO = "IPO"
    LONG = "Long"
    SHORT = "Short"


class Reason:
    Buy = 1
    Sell = 2
    Dividend = 3
    TranOut = 4
    TranIn = 5


class StockMaster(models.Model):
    class Meta:
        ordering = ['-add_date']

    project_choices = [
        (Project.IPO, "IPO"),
        (Project.LONG, "Long"),
        (Project.SHORT, "Short"),
    ]

    add_date = models.DateField()
    code = models.ForeignKey(StockCode)
    project = models.CharField(max_length=10, choices=project_choices)
    remark = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return "%s@%s" % (self.code.name_chi, self.remark)


class Transaction(models.Model):
    class Meta:
        ordering = ['-add_date']

    reason_choices = [
        (Reason.Buy, "Buy"),
        (Reason.Sell, "Sell"),
        (Reason.Dividend, "Dividend"),
        (Reason.TranOut, "TranOut"),
        (Reason.TranIn, "TranIn"),
    ]

    add_date = models.DateField()
    master = models.ForeignKey(StockMaster, null=True)
    money = models.DecimalField(max_digits=14, decimal_places=4)
    price = models.DecimalField(max_digits=14, decimal_places=4)
    quantity = models.PositiveSmallIntegerField()
    reason = models.PositiveSmallIntegerField(choices=reason_choices)
    broker = models.ForeignKey(Broker, null=True, blank=True)















