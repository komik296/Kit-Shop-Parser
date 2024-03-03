import mysql.connector

db_config = {
    'host': '80.85.242.53',
    'user': 'admin',
    'password': 'eZPLh#jLHctng8cN',
    'database': 'kit_vending_umvend',
    'port': '3306',  # По умолчанию 3306
}

def show_table_structure(table):
    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # Запрос для получения структуры таблицы
            query = f"DESCRIBE {table}"

            # Выполнение запроса
            cursor.execute(query)

            # Получение результатов запроса
            table_structure = cursor.fetchall()

            # Вывод структуры таблицы
            for column in table_structure:
                print(column)

    except mysql.connector.Error as e:
        print("Ошибка при работе с базой данных:", e)

    finally:
        # Закрытие соединения
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Соединение с базой данных закрыто")



# Вызов функции для отображения структуры таблицы
show_table_structure('month_revenue_ural')
