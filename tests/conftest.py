import pytest


@pytest.fixture
def in_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def transactions():
    return [
        {"id": 939719570,
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
        "to": "Счет 75651667383060284188"},
        {"id": 142554268,
        "state": "EXECUTED",
        "date": "2019-05-04T23:20:05.206878",
        "operationAmount": {
            "amount": "55114.93",
            "currency": {
                "name": "RUB",
                "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 15508645243227258542",
        "to": "Счет 75651665583060284188"},
        {"id": 772264268,
        "state": "EXECUTED",
        "date": "2019-07-04T23:20:05.206878",
        "operationAmount": {
            "amount": "77114.93",
            "currency": {
                "name": "RUB",
                "code": "RUB"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 7770864524322725",
        "to": "Счет 77651667383060284188"},
        {"id": 882264268,
        "state": "EXECUTED",
        "date": "2019-08-04T23:20:05.206878",
        "operationAmount": {
            "amount": "88114.93",
            "currency": {
                "name": "RUB",
                "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"}]
