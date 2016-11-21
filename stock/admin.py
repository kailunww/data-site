from django.contrib import admin

from .models import *


@admin.register(StockCode)
class StockCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "name_chi", "name_eng", "lot_size")
    # list_filter = ('is_enable',)


@admin.register(StockMaster)
class StockMasterAdmin(admin.ModelAdmin):
    # pass
    list_display = ("add_date", "code", "price", "project", "quantity", "money")
    search_fields = ("code__code", )


@admin.register(StockAdd)
class StockAddAdmin(admin.ModelAdmin):
    # pass
    list_display = ("add_date", "master", "price", "quantity", "money")
    search_fields = ("master__code__code", )


@admin.register(MoneyIn)
class MoneyInAdmin(admin.ModelAdmin):
    # pass
    list_display = ("add_date", "master", "price", "quantity", "money")
    search_fields = ("master__code__code", )


@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    # pass
    list_display = ("add_date", "master", "price",  "money")
    search_fields = ("master__code__code", )


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    # list_filter = ('is_enable',)
