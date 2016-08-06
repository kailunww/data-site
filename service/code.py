import os
import django
import sys


# sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datasite.settings")
django.setup()

from stock.models import *
import requests
from bs4 import BeautifulSoup

StockCode.objects.all().delete()
url = "https://www.hkex.com.hk/eng/market/sec_tradinfo/stockcode/eisdeqty.htm"
r = requests.get(url)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"class": "table_grey_border"})
for tr in table.find_all("tr")[1:]:
    tds = tr.find_all("td")
    code = tds[0].text
    name = tr.find("a").text
    lot_size = tds[2].text.replace(",", "")
    StockCode.objects.update_or_create(code=code, defaults=dict(
        name_eng=name,
        lot_size=lot_size
    ))
url2 = "https://www.hkex.com.hk/chi/market/sec_tradinfo/stockcode/eisdeqty_c.htm"
r = requests.get(url2)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"class": "table_grey_border"})
for tr in table.find_all("tr")[1:]:
    tds = tr.find_all("td")
    code = tds[0].text
    name = tr.find("a").text
    print(name)
    StockCode.objects.update_or_create(code=code, defaults=dict(
        name_chi=name,
    ))
