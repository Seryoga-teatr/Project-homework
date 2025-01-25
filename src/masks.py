def get_mask_card_number(card_number: int = 0) -> str:
    """Функция возвращения маски по номеру карты"""
    if type(card_number) is int and len(str(card_number)) == 16:
        mask_number = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
        return mask_number
    return 'Неверно введены данные'


def get_mask_account(account: int = 0) -> str:
    """Функция возвращает маску счета"""
    if type(account) is int and len(str(account)) == 20:
        mask_account = "**" + str(account)[-4:]
        return mask_account
    return 'Неверно введены данные'


# if __name__ == "__main__":
#    print(get_mask_card_number(1564487911112386))
#    print(get_mask_account(12345678901234567890))
