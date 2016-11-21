import os
import sys
import django
import json

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datasite.settings")
    django.setup()
    from stock.models import StockCode, StockMaster, StockAdd, MoneyIn, Dividend
    for master in StockMaster.objects.all():
        add_quantity = sum(x.quantity for x in master.stockadd_set.all())
        sell_quantity = sum(x.quantity for x in master.moneyin_set.all())
        div_quantity = sum(x.quantity for x in master.dividend_set.all())
        # print(master.code, master.quantity, add_quantity, sell_quantity)
        os_quantity = master.quantity + add_quantity + div_quantity - sell_quantity
        if os_quantity:
            print(master.code, os_quantity)

