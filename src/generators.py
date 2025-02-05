

def filter_by_currency(trans_actions: list[dict], currency: str):
    '''Функция-генератор возвращает транзакции заданной валюты'''
    transaction_filter_currency = filter(
        lambda x: x["operationAmount"]["currency"]["name"] == currency, trans_actions)
    while True:
        yield transaction_filter_currency


def transaction_descriptions(trans_actions: list[dict]):
    '''Функция-генератор возвращает описание операции'''
    temp = 0
    while True:
        transaction_description = trans_actions[temp]["description"]
        yield transaction_description
        temp += 1


# if __name__ == "__main__":
#     descriptions = transaction_descriptions(transactions)
#     for i in range(5):
#         print(next(descriptions))


