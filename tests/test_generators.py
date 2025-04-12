# import pytest
# from typing import Any
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict]) -> None:
    '''Тестирование фильтар трансакций фикстурой'''
    generator_f = filter_by_currency(transactions, "USD")
    assert list(next(generator_f)) == [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"},
        {"id": 142264268,
         "state": "EXECUTED",
         "date": "2019-04-04T23:20:05.206878",
         "operationAmount": {
             "amount": "79114.93",
             "currency": {
                 "name": "USD",
                 "code": "USD"}},
         "description": "Перевод со счета на счет",
         "from": "Счет 19708645243227258542",
         "to": "Счет 75651667383060284188"}]


def test_filter_by_currency_zero(transactions: list[dict]) -> None:
    '''Тестирование фильтар трансакций фикстурой - пустые данные'''
    generator_f = filter_by_currency([], "")
    assert list(next(generator_f)) == []


def test_filter_by_not_currency(transactions: list[dict]) -> None:
    '''Тестирование фильтар трансакций фикстурой - вид валюты отсутствует'''
    generator_f = filter_by_currency(transactions, "EUR")
    assert list(next(generator_f)) == []


def test_transaction_descriptions(transactions: list[dict]) -> None:
    '''Тестирование генератора описаний операций'''
    generator_t = transaction_descriptions(transactions)
    assert next(generator_t) == "Перевод организации"
    assert next(generator_t) == "Перевод со счета на счет"
    assert next(generator_t) == "Перевод со счета на счет"
    assert next(generator_t) == "Перевод с карты на карту"
    assert next(generator_t) == "Перевод организации"


def test_card_number_generator_st_fin() -> None:
    '''Тестирование генератора номеров карт: старт < финиш'''
    generator_t = card_number_generator(9999, 10005)
    assert next(generator_t) == "0000 0000 0000 9999"
    assert next(generator_t) == "0000 0000 0001 0000"
    assert next(generator_t) == "0000 0000 0001 0001"


def test_card_number_generator_fin_st() -> None:
    '''Тестирование генератора номеров карт: старт > финиш'''
    generator_t = card_number_generator(9999999999999999, 9999999999999997)
    assert next(generator_t) == "9999 9999 9999 9997"
    assert next(generator_t) == "9999 9999 9999 9998"
    assert next(generator_t) == "9999 9999 9999 9999"
