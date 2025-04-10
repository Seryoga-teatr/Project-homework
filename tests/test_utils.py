import os.path
from typing import Any
from unittest.mock import mock_open, patch

import pytest

from config import DATA_DIR
from src.utils import get_transactions


@patch('builtins.open', new_callable=mock_open, read_data='[1, 2, 3]')
@patch('json.load')
def test_get_transactions(mock_json_load: Any, mock_open: Any) -> None:
    '''Тестирование преобразования JSON-файла в список'''

    # Настраиваем mock для json.load с нормальными данными
    mock_json_load.return_value = [1, 2, 3]
    # Вызываем функцию и проверяем результат
    result = get_transactions('fake_file.json')
    assert result == [1, 2, 3]

    # Проверяем, что open был вызван с правильными аргументами
    mock_open.assert_called_once_with('fake_file.json', 'r', encoding='utf-8')

    # Проверяем, что json.load был вызван
    mock_json_load.assert_called_once()


pathname_1 = os.path.join(DATA_DIR, 'test.json')
pathname_2 = os.path.join(DATA_DIR, 'test_operation.json')


@pytest.mark.parametrize("variable, expected",
                         [(pathname_1, []),
                          (pathname_2, [])])
def test_get_bad_transactions(variable: str, expected: list) -> None:
    '''Тестирование преобразования JSON-файла в список
    1 - тест когда файл не найден;
    2 - тест с файлом не JSON'''
    assert get_transactions(variable) == expected
