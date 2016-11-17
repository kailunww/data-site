from django.contrib import admin

from .models import *


@admin.register(StockCode)
class StockCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "name_chi", "name_eng", "lot_size")
    # list_filter = ('is_enable',)


@admin.register(StockIn)
class StockInAdmin(admin.ModelAdmin):
    # pass
    list_display = ("add_date", "code", "price", "project", "quantity", "money")


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    # list_filter = ('is_enable',)
