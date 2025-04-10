import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("variable, expected",
                         [('Visa Gold 1234567890123456', 'Visa Gold 1234 56** **** 3456'),
                          ('Счет 12345678901234567890', 'Счет **7890'),
                          ('Visa Gold 123456789o123456', 'Неверно введены данные'),     # цифра-буква
                          ('Счет 1234567890123456789o', 'Неверно введены данные'),      # цифра-буква
                          ('Visa Gold 123456789012345', 'Неверно введены данные'),      # мало цифр
                          ('Счет 123456789012345678901', 'Неверно введены данные')])    # много цифр
def test_mask_account_card(variable: str, expected: str) -> None:
    '''Проверка вывода масок при помощи параметризации'''
    assert mask_account_card(variable) == expected


@pytest.mark.parametrize("variable, expected",
                         [('2024-03-11T02:26:18.671407', '11.03.2024'),
                          ('2028-15-33T02:26:18.671407', '33.15.2028'),
                          ('2000-00-00T02:26:18.671407', '00.00.2000')])
def test_get_date(variable: str, expected: str) -> None:
    '''Проверка вывода даты при помощи параметризации'''
    assert get_date(variable) == expected
