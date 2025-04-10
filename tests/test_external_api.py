import os
from typing import Any
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import transaction_amount_in_rub

transactions = {"id": 720751477,
                "operationAmount": {"amount": "10",
                                    "currency": {"name": "CAD",
                                                 "code": "CAD"}}}


@patch('requests.get')
def test_transaction_amount_in_rub(mock_get: Any) -> None:
    '''Тестирование конвертации с имитацией статус-кода и ответа от API'''
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 597.45844}
    assert mock_get.return_value.status_code == 200
    assert transaction_amount_in_rub(transactions) == 597.45844
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": "10", "from": "CAD", "to": "RUB"}
    load_dotenv()
    apikey = os.getenv('APIKEY')
    headers = {"apikey": apikey}
    mock_get.assert_called_once_with(url, headers=headers, params=payload)


@patch('requests.get')
def test_transaction_error_status_code(mock_get: Any) -> None:
    '''Тестирование конвертации с имитацией ошибки в статус-коде'''
    mock_get.return_value.status_code = 404
    assert mock_get.return_value.status_code == 404
    assert transaction_amount_in_rub(transactions) == 'Ошибка при запросе. Статус-код: 404!'


def test_transaction_rub_in_rub() -> None:
    '''Тестирование конвертации с некорректной валютой'''
    transactions = {"id": 720751477,
                    "operationAmount": {"amount": "10",
                                        "currency": {"name": "RUB",
                                                     "code": "RUB"}}}
    assert transaction_amount_in_rub(transactions) == 10.0


def test_transaction_error_currency_code() -> None:
    '''Тестирование конвертации с некорректной валютой'''
    transactions = {"id": 720751477,
                    "operationAmount": {"amount": "10",
                                        "currency": {"name": "CAD",
                                                     "code": "CADD"}}}
    assert transaction_amount_in_rub(transactions) == 'Ведена некорректная валюта: CADD!'
