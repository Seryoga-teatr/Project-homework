# from tests.conftest import transactions


def filter_by_currency(trans_actions: list[dict], currency: str):
    '''Функция-генератор возвращает транзакции заданной валюты'''
    temp = 0
    transaction_filter_currency = filter(
        lambda x: x["operationAmount"]["currency"]["name"] == currency, trans_actions)
    while True:
        yield transaction_filter_currency
        temp += 1


# usd_transactions = filter_by_currency(transactions, "USD")
# for i in range(2):
#    print(list(next(usd_transactions)))

