import mysql.connector
from config import db_config, table_name_revenue_and_sales_per_day
# Замените значения переменных на ваши настройки подключения

def create_table():
    # Подключение к базе данных
    connection = mysql.connector.connect(**db_config)

    # Создание курсора для выполнения SQL-запросов
    cursor = connection.cursor()


    #for name in table_name_revenue_and_sales_per_day.values():
    #print(name)
        #drop_table = f'DROP TABLE {name}'
    create_table_query = f"""
                CREATE TABLE IF NOT EXISTS umvend_revenue_today (
                    id_affiliate INT UNIQUE,
                    revenue DECIMAL(10, 3),
                    quantity DECIMAL(10, 3),
                    affiliate TEXT
                                               );
        
            """

            # Выполнение SQL-запроса для создания таблицы
        #cursor.execute(drop_table)
    cursor.execute(create_table_query)

    # Закрытие курсора и соединения
    cursor.close()
    connection.close()