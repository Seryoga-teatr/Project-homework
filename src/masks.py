def get_mask_card_number(card_number: int) -> str:
    """Функция возвращения маски по номеру карты"""
    mask_number = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
    return mask_number


def get_mask_account(account: int) -> str:
    """Функция возвращает маску счета"""
    mask_account = "**" + str(account)[-4:]
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number(1564487911112386))
    print(get_mask_account(654212318495846565465))
