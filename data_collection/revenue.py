import requests
import re
from bs4 import BeautifulSoup
import lxml

from config import headers, filter_params, cookies_affiliates

def data_rev_qua(affiliate):
    headers['Cookie'] = cookies_affiliates[affiliate]

    req_modems = requests.get('https://kitshop.ru/Reports/Sales', headers=headers)
    soup_modems = BeautifulSoup(req_modems.text, 'lxml')

    table = soup_modems.find('tfoot').text

    matches = re.findall('\d+', table)

    if len(matches) >= 2:
        quantity = matches[0]
        revenue = matches[1]
        print("Quantity:", quantity)
        print("Revenue:", revenue)
    else:
        print("Недостаточно совпадений для извлечения quantity и revenue.")
        quantity, revenue = 0, 0

    print(f'{affiliate} Показатели за сегодня {revenue}, {quantity}')

    return quantity, revenue

def data_rev_month(date_start, date_end, affiliate):
    headers['Cookie'] = cookies_affiliates[affiliate]

    filter_params['filter.UpDateString'] = date_start
    filter_params['filter.ToDateString'] = date_end

    req_modems = requests.post('https://kitshop.ru/Reports/Sales', headers=headers, data=filter_params)
    soup_modems = BeautifulSoup(req_modems.text, 'lxml')
    table = soup_modems.find('tfoot').text

    matches = re.findall('\d+', table)

    if len(matches) >= 2:
        quantity = matches[0]
        revenue = matches[1]
        print(f'{affiliate} Период:{date_start}-{date_end}\nRevenue: {revenue}; Quantity{quantity}')
    else:
        print("Недостаточно совпадений для извлечения quantity и revenue.")
        quantity, revenue = 0, 0

    return quantity, revenue



