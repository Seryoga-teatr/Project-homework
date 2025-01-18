from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_of_card: str) -> str:
    '''Маскировка названия карты или счета'''
    list_in_func = name_of_card.split(' ')
    if list_in_func[0] == 'Счет':
        list_in_func[-1] = get_mask_account(int(list_in_func[-1]))
    else:
        list_in_func[-1] = get_mask_card_number(int(list_in_func[-1]))
    return ' '.join(list_in_func)


def get_date(date_time_str: str) -> str:
    '''Вывод даты в формате: ДД.ММ.ГГГГ'''
    return date_time_str[8:10] + '.' + date_time_str[5:7] + '.' + date_time_str[0:4]


if __name__ == "__main__":
    print(mask_account_card('Visa Gold 599899414228426353'))
    print(mask_account_card('Счет 75136454108430135874305'))
    print(get_date('2024-03-11T02:26:18.671407'))
