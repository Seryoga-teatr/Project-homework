def filter_by_state(input_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    '''Фильтрует список словарей по ключу "state"'''
    out_list = []
    for i in input_list:
        if i['state'] == state:
            out_list.append(i)
    return out_list


def sort_by_date(input_list: list[dict], decreasing: bool = True) -> list[dict]:
    '''Сортирует список словарей по ключу "date"'''
    return sorted(input_list, key=lambda input_list: input_list['date'], reverse=decreasing)


# if __name__ == "__main__":
#    in_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#    print(filter_by_state(in_list, 'EXECUTED'))
#    print(sort_by_date(in_list))
