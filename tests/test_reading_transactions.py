from typing import Any
from unittest.mock import patch

from src.reading_transactions import get_transactions_csvfile, get_transactions_excelfile


@patch('src.reading_transactions.pd.read_csv')
def test_get_transactions_csvfile(mock_read_csv: Any) -> None:
    '''Тестирование считывания транзакций с имитацией чтения из файла'''
    mock_read_csv.return_value.to_dict.return_value = [{'id': 1.0, 'd': '2023'}, {'id': 2.0, 'd': '2020'}]
    assert get_transactions_csvfile('fake_file.csv') == [{'id': 1.0, 'd': '2023'}, {'id': 2.0, 'd': '2020'}]


@patch('src.reading_transactions.pd.read_excel')
def test_get_transactions_excelfile(mock_read_excel: Any) -> None:
    '''Тестирование считывания транзакций с имитацией чтения из файла'''
    mock_read_excel.return_value.to_dict.return_value = [{'id': 5.0, 'd': '2023'}, {'id': 8.0, 'd': '2020'}]
    assert get_transactions_excelfile('fake_file.csv') == [{'id': 5.0, 'd': '2023'}, {'id': 8.0, 'd': '2020'}]


def test_get_transactions_FileNotFound() -> None:
    '''Тестирование считывания транзакций с ошибкой FileNotFoundError'''
    assert get_transactions_csvfile('fake_file.csv') == []
    assert get_transactions_excelfile('fake_file.xlsx') == []
