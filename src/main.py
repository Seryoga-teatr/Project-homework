import os.path
import datetime
import re
# from collections.abc import generator

from config import DATA_DIR
# from mypy.state import state
from reading_transactions import get_transactions_excelfile, get_transactions_csvfile
from src.utils import get_transactions
from processing import filter_by_state, sort_by_date
from generators import filter_by_currency_1, filter_by_currency_2, transaction_descriptions
from process_bank import process_bank_search
from masks import get_mask_account, get_mask_card_number

print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:''')
while True:
    print('''
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла''')
    format_file:str = input('Выберите 1-3: ')
    if format_file == '1':
        print('Для обработки выбран JSON-файл.')
        pathname = os.path.join(DATA_DIR, 'operations.json')
        data_work = get_transactions(pathname)
        break
    elif format_file == '2':
        print('Для обработки выбран CSV-файл.')
        pathname = os.path.join(DATA_DIR, 'transactions.csv')
        data_work = get_transactions_csvfile(pathname)
        break
    elif format_file == '3':
        print('Для обработки выбран XLSX-файл.')
        pathname = os.path.join(DATA_DIR, 'transactions_excel.xlsx')
        data_work = get_transactions_excelfile(pathname)
        break
    else:
        print('Не корректный выбор, повторите.')

while True:
    print('''Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    filter_state: str = input()
    filter_state_lower = filter_state.lower()
    if filter_state_lower == 'executed':
        data_work_filter = filter_by_state(data_work)
        print('Операции отфильтрованы по статусу "EXECUTED".')
        break
    elif filter_state_lower == 'canceled':
        data_work_filter = filter_by_state(data_work, "CANCELED")
        print('Операции отфильтрованы по статусу "CANCELED".')
        break
    elif filter_state_lower == 'pending':
        data_work_filter = filter_by_state(data_work, "PENDING")
        print('Операции отфильтрованы по статусу "PENDING".')
        break
    else:
        print(f'Статус операции "{filter_state}" недоступен.')

user_date:str = ''
user_sort:str = ''
data_work_filter_sort = []
while True:
    if not data_work_filter:
        break
    user_date:str = input('Отсортировать операции по дате? Да/Нет ').lower()
    if user_date == 'да':
        while True:
            user_sort = input('Отсортировать по возрастанию или по убыванию? ').lower()
            if user_sort == 'по возрастанию':
                data_work_filter_sort = sort_by_date(data_work_filter, False)
                break
            elif user_sort == 'по убыванию':
                data_work_filter_sort = sort_by_date(data_work_filter)
                break
            else:
                print('Некорректный ввод, повторите.')
        break
    elif user_date == 'нет':
        data_work_filter_sort = data_work_filter
        break
    else:
        print('Не корректный выбор, повторите.')

data_work_filter_sort_currency:list = []
while True:
    if not data_work_filter_sort:
        break
    user_currency:str = input("Выводить только рублевые транзакции? Да/Нет ").lower()
    if user_currency == 'да':
        if format_file == '1':
            generator_f = filter_by_currency_1(data_work_filter_sort, "RUB")
        else:
            generator_f = filter_by_currency_2(data_work_filter_sort, "RUB")
        data_work_filter_sort_currency = list(next(generator_f))
        break
    elif user_currency == 'нет':
        data_work_filter_sort_currency = data_work_filter_sort
        break
    else:
        print('Некорректный ввод, повторите.')

data_work_filter_sort_cur_desc:list[dict] = []
while True:
    if not data_work_filter_sort_currency:
        break
    user_word:str = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").lower()
    if user_word == 'да':
        descriptions = transaction_descriptions(data_work_filter_sort_currency)
        descr_for_out = []
        for i in data_work_filter_sort_currency:
            if i["description"] not in descr_for_out:
                descr_for_out.append(i["description"])
            next(descriptions)
        print('Список для выбора описания:')
        for num in range(len(descr_for_out)):
            print(num+1, descr_for_out[num])
        user_num = int(input('Выберите номер позиции: '))
        print(descr_for_out[user_num-1])
        data_work_filter_sort_cur_desc = process_bank_search(data_work_filter_sort_currency, descr_for_out[user_num-1])
        break
    elif user_word == 'нет':
        data_work_filter_sort_cur_desc = data_work_filter_sort_currency
        break
    else:
        print('Некорректный ввод, повторите.')

if data_work_filter_sort_cur_desc:
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(data_work_filter_sort_cur_desc)}')
    for i in (data_work_filter_sort_cur_desc):
        date_string = i['date']
        if format_file == '1':
            date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
        date_string = date_obj.strftime("%d.%m.%Y")
        print('')
        print(date_string, i['description'])

        i_from = i.get('from')
        i_to = ''
        # nomer = ''
        if type(i_from) == str:
            pattern = r'\d+'
            string = i_from
            nomer = re.search(pattern, string, flags=0)
            if len(nomer.group()) == 20:
                i_from = i_from[:-20] + get_mask_account(int(nomer.group()))
            elif len(nomer.group()) == 16:
                i_from = i_from[:-16] + get_mask_card_number(int(nomer.group()))
            print(i_from, '->', end=' ')

        pattern = r'\d+'
        string = i['to']
        nomer = re.search(pattern, string, flags=0)
        if len(nomer.group()) == 20:
            i_to = i['to'][:-20] + get_mask_account(int(nomer.group()))
        elif len(nomer.group()) == 16:
            i_to = i['to'][:-16] + get_mask_card_number(int(nomer.group()))

        print(i_to)
        if format_file == '1':
            print(f'Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['code']}')
        else:
            print(f'Сумма: {i['amount']} {i['currency_code']}')
else:
    print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
