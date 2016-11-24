import requests
import datetime
from decimal import Decimal


def get_price(code):
    if str(code).startswith("0"):
        code = code[1:]
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s.HK&f=sl1d1t1c1ohgv&e=.csv" % code
    r = requests.get(url)
    data = r.text.split(",")
    price = Decimal(data[1])
    dt_string = "%s %s" % (data[2], data[3])
    dt = datetime.datetime.strptime(dt_string, '"%m/%d/%Y" "%I:%M%p"')
    # print(price, dt)
    return price, dt


def get_dividend_history(code, start_date):
    if str(code).startswith("0"):
        code = code[1:]
    url = "http://real-chart.finance.yahoo.com/table.csv?s=%s.HK&g=v&ignore=.csv" % code
    r = requests.get(url)
    # print(url)
    lines = r.iter_lines()
    div_list = []
    lines.__next__()
    for line in lines:
        # print(line)
        div_date, price = line.decode().split(",")
        if div_date <= start_date:
            break
        div_list.append((div_date, price))
    return div_list
