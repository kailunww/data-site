from django.contrib import admin

from .models import *


@admin.register(StockCode)
class StockCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "name_chi", "name_eng", "lot_size")
    # list_filter = ('is_enable',)


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    # list_filter = ('is_enable',)
