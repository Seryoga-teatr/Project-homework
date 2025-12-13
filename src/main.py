import os.path

from config import DATA_DIR
# from mypy.state import state
from reading_transactions import get_transactions_excelfile, get_transactions_csvfile
from src.utils import get_transactions
from processing import filter_by_state, sort_by_date
from generators import filter_by_currency


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


user_sort:str = ' '
data_work_filter_sort = []
while True:
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

data_work_filter_sort_currency = []
while True:
    user_currency:str = input("Выводить только рублевые транзакции? Да/Нет").lower()
    if user_currency == 'да':
        data_work_filter_sort_currency = filter_by_currency(data_work_filter_sort, "руб.")
        break
    elif user_currency == 'нет':
        data_work_filter_sort_currency = data_work_filter_sort
        break
    else:
        print('Некорректный ввод, повторите.')

data_work_filter_sort_cur_desc = []
while True:
    user_word:str = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
    if user_word == 'да':
        user_description:str = input("Введите слово в описании: ").lower()

        break
    elif user_word == 'нет':
        data_work_filter_sort_cur_desc = data_work_filter_sort_currency
        break
    else:
        print('Некорректный ввод, повторите.')

if data_work_filter_sort_cur_desc:
    print('Распечатываю итоговый список транзакций...')
    print('Всего банковских операций в выборке: 4')
else:
    print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')


print(format_file, filter_state_lower, user_date, user_sort)
print(len(data_work_filter_sort))
print(data_work_filter_sort[:2])
