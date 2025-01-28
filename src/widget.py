from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_of_card: str) -> str:
    '''Маскировка названия карты или счета'''
    list_in_func = name_of_card.split(' ')

    try:
        if list_in_func[0] == 'Счет':
            list_in_func[-1] = get_mask_account(int(list_in_func[-1]))
        else:
            list_in_func[-1] = get_mask_card_number(int(list_in_func[-1]))
    except ValueError:
        return "Неверно введены данные"

    if list_in_func[-1] == 'Неверно введены данные':
        return "Неверно введены данные"

    return ' '.join(list_in_func)


def get_date(date_time_str: str) -> str:
    '''Вывод даты в формате: ДД.ММ.ГГГГ'''
    return date_time_str[8:10] + '.' + date_time_str[5:7] + '.' + date_time_str[0:4]


# if __name__ == "__main__":
#    print(mask_account_card('Visa Gold 1234567890123456'))
#    print(mask_account_card('Счет 12345678901234567890'))
#    print(get_date('2024-03-11T02:26:18.671407'))
