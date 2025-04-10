# from typing import Generator, Iterable
from typing import Any, Dict, Generator


def filter_by_currency(trans_actions: list[Dict[str, Any]], currency: str) -> Generator[filter, None, None]:
    '''Функция-генератор возвращает транзакции заданной валюты Generator[filter[Dict[str, Any]], None, None]'''
    transaction_filter_currency = filter(
        lambda x: x.get("operationAmount", {}).get("currency", {}).get("name") == currency, trans_actions)
    while True:
        yield transaction_filter_currency


def transaction_descriptions(trans_actions: list[dict]) -> Generator[str, None, None]:
    '''Функция-генератор возвращает описание операции'''
    temp = 0
    while True:
        transaction_description = trans_actions[temp]["description"]
        yield transaction_description
        temp += 1


def card_number_generator(start: int, finish: int) -> Generator[str, None, None]:
    '''Функция-генератор номеров банковских карт'''
    if start > finish:
        start, finish = finish, start
    while start <= finish:
        num_str = str("{:016d}".format(start))
        result = num_str[:4] + ' ' + num_str[4:8] + ' ' + num_str[8:12] + ' ' + num_str[-4:]
        yield result
        start += 1

# for card_number in card_number_generator(12345678901234561, 12345678901234565):
#     print(card_number)


# if __name__ == "__main__":
#     trans__ = [{
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"}, {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"}, {
#         "id": 142554268,
#         "state": "EXECUTED",
#         "date": "2019-05-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "55114.93",
#             "currency": {
#                 "name": "RUB",
#                 "code": "RUB"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 15508645243227258542",
#         "to": "Счет 75651665583060284188"}, {
#         "id": 772264268,
#         "state": "EXECUTED",
#         "date": "2019-07-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "77114.93",
#             "currency": {
#                 "name": "RUB",
#                 "code": "RUB"}},
#         "description": "Перевод с карты на карту",
#         "from": "Счет 7770864524322725",
#         "to": "Счет 77651667383060284188"}, {
#         "id": 882264268,
#         "state": "EXECUTED",
#         "date": "2019-08-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "88114.93",
#             "currency": {
#                 "name": "RUB",
#                 "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"}]
#     generator_f = filter_by_currency(trans__, "RUB")
#     print(list(next(generator_f)))

#     descriptions = transaction_descriptions(transactions)
#     for i in range(5):
#         print(next(descriptions))
