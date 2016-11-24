from django.contrib import admin

from .models import *


@admin.register(StockCode)
class StockCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "name_chi", "name_eng", 'latest_price', 'last_update', "lot_size")
    list_filter = ('last_update',)


@admin.register(StockMaster)
class StockMasterAdmin(admin.ModelAdmin):
    # pass
    list_display = ("add_date", "code",  "project",)
    search_fields = ("code__code", )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    # pass
    list_display = ("add_date", "reason", "master", "broker", "price", "quantity", "money")
    search_fields = ("master__code__code", "reason")
    list_filter = ('reason', "add_date")
    raw_id_fields = ("master",)


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    # list_filter = ('is_enable',)
