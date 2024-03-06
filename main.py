import time
from datetime import datetime, timedelta, timezone
import requests
from datetime import datetime, timedelta, date
from mysql.connector import errors

from config import AUTHORIZATION, affiliates_id, affiliates_utc, cookies_affiliates, currency_date_update
from database.create_table import create_table
from database.kit_vending_ural import umvend_ural_indicators, revenue_and_sales_days
from auth.auth import authorizetion
from data_collection.revenue import data_rev_qua, data_rev_month
from other.date_work import get_first_and_last_day_of_month


if __name__ == '__main__':

    time_utc_func = lambda x: (datetime.now(timezone.utc) + timedelta(hours=x))

    for affiliate in affiliates_utc:
        login, password = AUTHORIZATION[affiliate]
        print(login, password, affiliate)
        authorizetion(login, password, affiliate)
        time.sleep(10)


    while True:

        for affiliate, utc_size in affiliates_utc.items():  # Урал correct affiliates_utc.items
            try:

                today_utc = time_utc_func(utc_size).date()
                affiliate_id = int(affiliates_id[affiliate])

                if currency_date_update[affiliate] < today_utc:
                    print('Начал обновлять продажи за вчерашний день', affiliate)

                    date_correct_mysql = (today_utc - timedelta(days=1))
                    date_site = date_correct_mysql.strftime('%d.%m.%Y')

                    qua_day, rev_day = data_rev_month(date_site, date_site, affiliate)

                    revenue_and_sales_days(affiliate, (rev_day, qua_day, date_correct_mysql))

                    currency_date_update[affiliate] = today_utc
                    print('Обновил продажи за вчерашний день', affiliate)

                quantity, revenue = data_rev_qua(affiliate)

                umvend_ural_indicators("umvend_revenue_today", (affiliate_id, revenue, quantity, affiliate))

                print(affiliate, 'Завершен и спит')
                time.sleep(100)

            except AttributeError as err:
                if err.name != 'text':  # Закончились куки
                    raise AttributeError(err)

                login, password = AUTHORIZATION[affiliate]
                authorizetion(login, password, affiliate)

            except ValueError as err:
                if "too many values to unpack" not in str(err):
                    raise ValueError(err)

                print(err)
                login, password = AUTHORIZATION[affiliate]
                authorizetion(login, password, affiliate)

        print("Цикл закончен")
        time.sleep(110)

