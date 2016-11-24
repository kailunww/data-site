import os
import sys
import django
import json

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datasite.settings")
    django.setup()
    from stock.models import StockCode, StockMaster, Transaction, Reason
    # for master in StockMaster.objects.all().order_by("code__code"):
    #     quantity = sum(x.quantity for x in master.transaction_set.all())
    #     money = sum(x.money for x in master.transaction_set.all())
    #     if quantity:
    #         print(master.code, master.remark, quantity, money)
    master_list = StockMaster.objects.all().order_by("code__code")
    updated = []
    import yahoo
    # for master in master_list:
    #     code = master.code
    #     if code in updated:
    #         continue
    #     price, last_update = yahoo.get_price(code.code)
    #     code.latest_price = price
    #     code.last_update = last_update
    #     code.save()
    #     updated.append(code)
    for master in master_list:
        code = master.code
        quantity = sum(x.quantity for x in master.transaction_set.all())
        if not quantity:
            continue
        print(code,  master.code.name_chi)
        div_history = yahoo.get_dividend_history(code.code, str(master.add_date))
        div_count = master.transaction_set.filter(reason=Reason.Dividend).count()

        print(len(div_history), div_count)

