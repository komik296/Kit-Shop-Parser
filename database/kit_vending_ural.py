import mysql.connector
from config import db_config, table_name_revenue_and_sales_per_day

# Замените значения переменных на ваши настройки подключения

def umvend_ural_revenue(val):
    # Подключение к базе данных
    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()


    # SQL-запрос для добавления данных в таблицу
    sql = "INSERT INTO umvend_ural_revenue (revenue, quantity, date) VALUES (%s, %s, %s)"


    # Выполнение запроса
    cursor.execute(sql, val)

    # Подтверждение изменений в базе данных
    connection.commit()

    print(cursor.rowcount, "запись добавлена")

    # Пример выполнения SQL-запроса
    cursor.execute("SELECT * FROM umvend_ural_revenue")

    # Получение результатов запроса
    rows = cursor.fetchall()

    # Вывод результатов запроса
    for row in rows:
        print(row)

    # Закрытие курсора
    cursor.close()


    connection.close()

def umvend_ural_revenue_month(val):
    # Подключение к базе данных
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # SQL-запрос для добавления данных в таблицу
    sql = f"INSERT INTO month_revenue (revenue, quantity, month_name, date_selection, affiliate) VALUES (%s, %s, %s, %s, %s)"

    # Выполнение запроса
    cursor.execute(sql, val)
    connection.commit()

    # Закрытие курсора
    cursor.close()
    connection.close()

def umvend_ural_indicators(name_table, val):
    # Подключение к базе данных
    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()


    # SQL-запрос для добавления данных в таблицу
    sql = f"""
        INSERT INTO {name_table} (id_affiliate, revenue, quantity, affiliate) 
            VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE id_affiliate = VALUES(id_affiliate), revenue = VALUES(revenue),
                    quantity = VALUES(quantity), affiliate = VALUES(affiliate)
    """



    # Выполнение запроса
    cursor.execute(sql, val)

    # Подтверждение изменений в базе данных
    connection.commit()



    # Пример выполнения SQL-запроса
    cursor.execute(f"SELECT * FROM {name_table}")

    # Получение результатов запроса
    rows = cursor.fetchall()

    # Вывод результатов запроса
    for row in rows:
        print(row)

    # Закрытие курсора
    cursor.close()


    connection.close()

def select_coffee_yestoday():
    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM umvend_ural_indicators_yesterday")

    results = cursor.fetchall()

    id, uniq_id, rev, qua = results[0]

    cursor.close()

    return (rev, qua)

def umvend_ural_revenue_year(val):
    # Подключение к базе данных
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # SQL-запрос для добавления данных в таблицу
    sql = """
                INSERT INTO every_month_revenue (revenue, quantity, start_date, affiliate)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE revenue = VALUES(revenue), quantity = VALUES(quantity);
          """

    # Выполнение запроса
    cursor.execute(sql, val)
    connection.commit()

    # Закрытие курсора
    cursor.close()
    connection.close()



def revenue_and_sales_days(affialate, val):
    # Подключение к базе данных

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    name_table = table_name_revenue_and_sales_per_day[affialate]

    # SQL-запрос для добавления данных в таблицу
    sql = f"""
                INSERT INTO {name_table} (revenue, sales, date)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE revenue = VALUES(revenue), sales = VALUES(sales);
          """

    # Выполнение запроса
    cursor.execute(sql, val)
    connection.commit()

    # Закрытие курсора
    cursor.close()
    connection.close()