import pandas as pd

# import csv
# import os.path
# from config import DATA_DIR


def get_transactions_csvfile(path_name: str) -> list:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с транзакциями"""
    transactions_reviews: list[dict] = []
    try:
        transactions_reviews = pd.read_csv(path_name, sep=';').to_dict(orient='records')
    except FileNotFoundError:
        print('Файл не найден.')
    # except pd.errors.EmptyDataError:
    #     print("Файл пуст. Пожалуйста, проверьте содержимое файла.")
    # except pd.errors.ParserError:
    #     print("Ошибка парсинга данных. Проверьте формат файла.")
    # except Exception as e:
    #     print(f"Произошла ошибка: {e}")
    return transactions_reviews


def get_transactions_excelfile(path_name: str) -> list:
    """Принимает на вход путь до excel-файла и возвращает список словарей с транзакциями"""
    transactions_reviews: list[dict] = []
    try:
        transactions_reviews = pd.read_excel(path_name).to_dict(orient='records')
    except FileNotFoundError:
        print('Файл не найден.')
    return transactions_reviews


# if __name__ == "__main__":
#
#     pathname = os.path.join(DATA_DIR, 'transactions_excel.xlsx')
#     data_exc = get_transactions_excelfile(pathname)
#
#     pathname = os.path.join(DATA_DIR, 'transactions.csv')
#     data_csv = get_transactions_csvfile(pathname)
#
#     print(len(data_csv), len(data_exc))
#     print(data_csv[:2])
#     print(data_exc[:2])
