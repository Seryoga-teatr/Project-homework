import json

# import os.path
# from config import DATA_DIR


def get_transactions(path_name: str) -> list:
    '''Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    data: list[dict] = []   # файл пустой, если содержит не список или не найден
    try:
        with open(path_name, 'r', encoding='utf-8') as f:
            try:
                json_data: list[dict] = json.load(f)
            except json.JSONDecodeError:
                return data
    except FileNotFoundError:
        return data
    if type(json_data) is list:
        return json_data
    return data


# if __name__ == "__main__":
#     pathname = os.path.join(DATA_DIR, 'test_operations.json')
#     print(pathname)
#     print(get_transactions(pathname))
