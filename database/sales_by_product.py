import csv
import mysql.connector
from config import db_config



def read_list_and_insert_to_mysql(name_table, affiliate, data):
    try:
        # Подключение к MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()


        for row in data:


            # Добавление данных в MySQL
            query = f"""
            INSERT INTO {name_table} (id, name_product, quantity, sum, availability, cashless, 
                                          other, revenue_share, affiliate)            
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE 
                        id = VALUES(id), name_product = VALUES(name_product), quantity = VALUES(quantity), 
                        sum = VALUES(sum), availability = VALUES(availability), cashless = VALUES(cashless), 
                        other = VALUES(other), revenue_share = VALUES(revenue_share), affiliate = VALUES(affiliate)
            """

            cursor.execute(query, tuple(row.values()) + (affiliate,))

        # Фиксация изменений и закрытие соединения
        connection.commit()
        print("Данные успешно загружены в MySQL.")

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")

    finally:
        # Закрытие соединения с MySQL
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

