def filter_by_currency(trans_actions: list[dict], currency: str):
    '''Функция-генератор возвращает транзакции заданной валюты'''
    transaction_filter_currency = filter(
        lambda x: x.get("operationAmount", {}).get("currency", {}).get("name") == currency, trans_actions)
    while True:
        yield transaction_filter_currency


def transaction_descriptions(trans_actions: list[dict]):
    '''Функция-генератор возвращает описание операции'''
    temp = 0
    while True:
        transaction_description = trans_actions[temp]["description"]
        yield transaction_description
        temp += 1


def card_number_generator(start: int, finish: int):
    '''Функция-генератор номеров банковских карт'''
    if start > finish:
        start, finish = finish, start
    while start <= finish:
        num_str = str("{:016d}".format(start))
        result = num_str[:4] + ' ' + num_str[4:8] + ' ' + num_str[8:12] + ' ' + num_str[-4:]
        yield result
        start += 1

# for card_number in card_number_generator(12345678901234561, 12345678901234565):
#     print(card_number)

# if __name__ == "__main__":
#     descriptions = transaction_descriptions(transactions)
#     for i in range(5):
#         print(next(descriptions))
