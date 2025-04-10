import os
from typing import Any

import requests
from dotenv import load_dotenv


def transaction_amount_in_rub(transactions: dict) -> Any:
    '''Конвертация суммы транзакции в рубли с использованием ресурса api.apilayer.com'''
    currency_code = transactions['operationAmount']['currency']['code']
    currency_amount = transactions['operationAmount']['amount']

    currency_code_list = ['RUB', 'USD', 'EUR', 'GBP', 'JPY', 'CAD', 'CHF']

    if currency_code == 'RUB':
        return float(currency_amount)
    elif currency_code in currency_code_list:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": currency_amount,
            "from": currency_code,
            "to": "RUB"
        }
        load_dotenv()
        apikey = os.getenv('APIKEY')
        headers = {
            "apikey": apikey
        }
        response = requests.get(url, headers=headers, params=payload)
        status_code = response.status_code

        if status_code == 200:
            result = response.json()
            return float(result['result'])

        # print(f'Ошибка при запросе. Статус-код: {status_code}!')
        return f'Ошибка при запросе. Статус-код: {status_code}!'

    # print(f'Ведена некорректная валюта: {currency_code}!')
    return f'Ведена некорректная валюта: {currency_code}!'


# if __name__ == "__main__":
#     transactions = {
#         "id": 720751477,
#         "state": "EXECUTED",
#         "date": "2018-11-08T08:21:45.902633",
#         "operationAmount": {
#             "amount": "10",
#             "currency": {
#                 "name": "USD",
#                 "code0": "USD",
#                 "code1": "RUB",
#                 "code": "CAD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75743795418434298755",
#         "to": "Счет 80785963509390811744"
#     }
#     print(transaction_amount_in_rub(transactions))
