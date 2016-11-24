import os
import sys
import django
import json

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datasite.settings")
    django.setup()
    from stock.models import StockCode, StockMaster, Transaction, Reason
    from stock.init_data import stock_in, stock_in_headers
    data = [dict(zip(stock_in_headers, m)) for m in stock_in.copy()]
    buffer = []
    StockMaster.objects.all().delete()
    for row in data:
        try:
            row["code"] = StockCode.objects.get(pk="0%s" % row["code"])
        except:
            print(row["code"])
            continue
        key = "%s-%s" % (row["code"], row.pop("sn"))
        row.pop("price")
        row.pop("quantity")
        row.pop("money")
        try:
            StockMaster.objects.get(remark=key)
        except StockMaster.DoesNotExist:
            StockMaster.objects.create(**row, remark=key)
    # StockMaster.objects.bulk_create(buffer)
    buffer = []
    data = [dict(zip(stock_in_headers, m)) for m in stock_in.copy()]
    buffer = []
    for row in data:
        try:
            row["code"] = StockCode.objects.get(pk="0%s" % row["code"])
        except:
            print(row["code"])
            continue
        key = "%s-%s" % (row.pop("code"), row.pop("sn"))
        row.pop("project")
        row["money"] = -row["money"]
        master_s = StockMaster.objects.get(remark=key)
        buffer.append(Transaction(**row, master=master_s, reason=Reason.Buy))
    Transaction.objects.all().delete()
    Transaction.objects.bulk_create(buffer)
    from stock.init_data import money_in, money_in_headers
    data = [dict(zip(money_in_headers, m)) for m in money_in]
    buffer = []
    for row in data:
        try:
            row["code"] = StockCode.objects.get(pk="0%s" % row["code"])
        except:
            print(row["code"])
            continue
        key = "%s-%s" % (row.pop("code"), row.pop("sn"))
        master_s = StockMaster.objects.get(remark=key)
        row["quantity"] = -row["quantity"]
        buffer.append(Transaction(**row, master=master_s, reason=Reason.Sell))
    # Transaction.objects.all().delete()
    Transaction.objects.bulk_create(buffer)
    from stock.init_data import dividend_in, dividend_in_headers
    data = [dict(zip(dividend_in_headers, m)) for m in dividend_in]
    buffer = []
    for row in data:
        try:
            row["code"] = StockCode.objects.get(pk="0%s" % row["code"])
        except:
            print(row["code"])
            continue
        key = "%s-%s" % (row.pop("code"), row.pop("sn"))
        master_s = StockMaster.objects.get(remark=key)
        row.pop("project")
        # row.pop("quantity")
        row["money"] = -row["money"]
        buffer.append(Transaction(**row, master=master_s, reason=Reason.Dividend))
    # Transaction.objects.all().delete()
    Transaction.objects.bulk_create(buffer)

