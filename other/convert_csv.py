import pandas as pd

def xls_to_csv(input_file, output_file):
    try:
        # Указываем openpyxl в качестве движка для чтения Excel
        df = pd.read_excel(input_file, engine='openpyxl')

        # Сохранение данных в CSV
        df.to_csv(output_file, index=False)

        print(f"Конвертация успешно завершена. Результат сохранен в {output_file}")
    except Exception as e:
        print(f"Произошла ошибка при конвертации: {e}")

# Пример использования
input_excel_file = "input.xlsx"  # Укажите путь к вашему файлу XLSX
output_csv_file = "../test.csv"  # Укажите путь, по которому нужно сохранить CSV

xls_to_csv(input_excel_file, output_csv_file)
