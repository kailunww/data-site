import os
import sys
import django
import json

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datasite.settings")
    django.setup()
    from stock.models import StockCode, StockIn
    # d = json.load(open("stock_code.data"))
    # buffer = []
    # for row in d:
    #     buffer.append(StockCode(**row))
    # StockCode.objects.bulk_create(buffer)
    from stock.init_data import stock_in, stock_in_headers
    data = [dict(zip(stock_in_headers, m)) for m in stock_in]
    print(data)
    buffer = []
    for row in data:
        try:
            row["code"] = StockCode.objects.get(pk="0%s" % row["code"])
        except:
            print(row["code"])
            continue
        buffer.append(StockIn(**row))
    StockIn.objects.all().delete()
    StockIn.objects.bulk_create(buffer)

