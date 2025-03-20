import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("variable, expected",
                         [(1234567890123456, '1234 56** **** 3456'),
                          (12345678901234567, 'Неверно введены данные'),
                          ('1234567890123456', 'Неверно введены данные'),
                          (None, 'Неверно введены данные')])
def test_get_mask_card_number(variable, expected):
    '''Тестирование выода маски карты при помощи параметризации'''
    assert get_mask_card_number(variable) == expected


@pytest.mark.parametrize("variable, expected",
                         [(12345678901234567890, '**7890'),
                          (1234567890123456789, 'Неверно введены данные'),
                          ('12345678901234567890', 'Неверно введены данные'),
                          (None, 'Неверно введены данные')])
def test_get_mask_account(variable, expected):
    '''Тестирование вывода маски счета при помощи параметризации'''
    assert get_mask_account(variable) == expected
