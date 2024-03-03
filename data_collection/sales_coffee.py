from bs4 import BeautifulSoup
import requests

from config import headers, cookies_affiliates


def convert_percentage_to_float(percentage_str):
    # Функция для конвертации строки с процентом в число
    return float(percentage_str.replace('%', '').replace(',', '.'))

def convert_float(percentage_str):
    return float(percentage_str.replace(',', '.'))


def sales_coffee_list(affiliate):
    headers['Cookie'] = cookies_affiliates[affiliate]

    url = "https://cabinet.kitvending.ru/Statistics/ExportSalesByGoods"

    # Запрос
    response = requests.get(url, headers=headers)

    # Парсинг HTML
    soup = BeautifulSoup(response.text, "lxml")

    # Нахождение таблицы
    table = soup.find("table")

    # Обработка строк
    data = []
    for row in table.find_all("tr"):
        # Пропуск заголовка
        if row.find("th"):
            continue

        # Извлечение данных
        cells = row.find_all("td")
        item = {
            "id": int(cells[0].text),
            "name_product": cells[1].text,
            "quantity": int(cells[2].text),
            "sum": convert_float(cells[3].text),
            'availability': convert_float(cells[4].text),
            'cashless': convert_float(cells[5].text),
            'other': convert_float(cells[6].text),
            'revenue_share': convert_percentage_to_float(cells[7].text)

        }

        data.append(item)

    return data


