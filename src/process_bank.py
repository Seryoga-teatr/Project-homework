# import os
import re

from reading_transactions import get_transactions_excelfile
from config import DATA_DIR
from collections import Counter

# 'description': 'Перевод организации'
#   [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
#      'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
#      'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
#     {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
#      'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
#      'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}]


def process_bank_search(data_list_dict:list[dict], search_description:str)->list[dict]:
    """функция принимать список словарей с данными и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка"""
    out_list = []
    pattern = search_description
    for data_dict in data_list_dict:
        string = data_dict['description']
        if type(string) == str:
            if re.search(pattern, string, flags=re.IGNORECASE):
                out_list.append(data_dict)
    return out_list


def process_bank_operations(data_list_dict: list[dict], categories: list[str]) -> dict[str, int]:
    """функцию принимает список словарей с данными и список категорий операций, возвращает словарь:
    ключи — названия категорий, значения — количество операций в каждой категории"""
    category_list = [operation['description'] for operation in data_list_dict if operation['description'] in categories]
    category_count = Counter(category_list)
    return dict(category_count)


# if __name__ == "__main__":
#     pathname = os.path.join(DATA_DIR, 'transactions_excel.xlsx')
#     data_exc = get_transactions_excelfile(pathname)
#
#     categories = ['Открытие вклада', 'Перевод организации', 'Перевод с карты на карту', 'Перевод со счета на счет']
#     result_dict = process_bank_operations(data_exc, categories)
#     print(result_dict)
#
#     search_d = 'Перевод с карты на карту'
#     data_search = process_bank_search(data_exc, search_d)
#     print(len(data_exc), len(data_search))
#     for i in range(10):
#         print(data_search[i])
