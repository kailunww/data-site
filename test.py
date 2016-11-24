import requests
import datetime
from decimal import Decimal


start_date = "2015-10-01"
code = "0005"
url = "http://real-chart.finance.yahoo.com/table.csv?s=%s.HK&g=v&ignore=.csv" % code

r = requests.get(url)
lines = r.iter_lines()
div_list = []
lines.__next__()
for line in lines:
    div_date, price = line.decode().split(",")
    if div_date <= start_date:
        break
    div_list.append((div_date, price))
print(div_list)
# url = "http://real-chart.finance.yahoo.com/table.csv?s=%s.HK&g=d&ignore=.csv" % code
#
# r = requests.get(url)
# print(r.text)


