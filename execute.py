import os
import sys
import django
import json

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datasite.settings")
    django.setup()
    from stock.models import StockCode, StockMaster, StockAdd, MoneyIn
    # d = json.load(open("stock_code.data"))
    # buffer = []
    # for row in d:
    #     buffer.append(StockCode(**row))
    # StockCode.objects.bulk_create(buffer)
    master_list = {}
    from stock.init_data import stock_in, stock_in_headers
    data = [dict(zip(stock_in_headers, m)) for m in stock_in]
    print(data)
    buffer_master = []
    add_data = []
    for row in data:
        try:
            row["code"] = StockCode.objects.get(pk="0%s" % row["code"])
        except:
            print(row["code"])
            continue
        key = "%s-%s" % (row["code"], row["sn"])
        row.pop("sn")
        if key not in master_list:
            master_list[key] = (row["code"], row["add_date"])
            row["remark"] = key
            buffer_master.append(StockMaster(**row))
        else:
            add_data.append((row, master_list[key]))
    StockMaster.objects.all().delete()
    StockMaster.objects.bulk_create(buffer_master)
    buffer_add = []
    for row, master in add_data:
        code, add_date = master
        row.pop("code")
        row.pop("project")
        master_s = StockMaster.objects.get(code=code, add_date=add_date)
        buffer_add.append(StockAdd(**row, master=master_s))
    StockAdd.objects.all().delete()
    StockAdd.objects.bulk_create(buffer_add)
    from stock.init_data import money_in, money_in_headers
    data = [dict(zip(money_in_headers, m)) for m in money_in]
    buffer_money = []
    for row in data:
        try:
            row["code"] = StockCode.objects.get(pk="0%s" % row["code"])
        except:
            print(row["code"])
            continue
        key = "%s-%s" % (row.pop("code"), row.pop("sn"))
        master_s = StockMaster.objects.get(remark=key)
        buffer_money.append(MoneyIn(**row, master=master_s))
    MoneyIn.objects.all().delete()
    MoneyIn.objects.bulk_create(buffer_money)
    from stock.init_data import dividend_in, dividend_in_headers
    from stock.models import Dividend
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
        buffer.append(Dividend(**row, master=master_s))
    Dividend.objects.all().delete()
    Dividend.objects.bulk_create(buffer)

