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

