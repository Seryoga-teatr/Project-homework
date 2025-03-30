import json
# import os.path
# from config import DATA_DIR


def get_transactions(path_name: str) -> list:
    '''Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    data = [] # файл пустой, содержит не список или не найден
    try:
        with open(path_name, 'r', encoding='utf-8') as f:
            try:
                json_data = json.load(f)
            except json.JSONDecodeError:
                return data
    except FileNotFoundError:
        return data
    return json_data

# if __name__ == "__main__":
#     pathname = os.path.join(DATA_DIR, 'operations.json')
#     print(pathname)
#     print(get_transactions(pathname))
