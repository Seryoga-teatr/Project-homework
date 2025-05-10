import json
import logging
import os.path

from config import LOGS_DIR

# from config import DATA_DIR, LOGS_DIR


utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
utils_path = os.path.join(LOGS_DIR, 'utils.log')
file_handler = logging.FileHandler(utils_path, mode="w", encoding='utf-8')
file_formater = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
utils_logger.addHandler(file_handler)


def get_transactions(path_name: str) -> list:
    '''Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    utils_logger.info('Вызов функции транзакций: get_transactions')
    data: list[dict] = []   # файл пустой, если содержит не список  или не найден
    try:
        with open(path_name, 'r', encoding='utf-8') as f:
            try:
                json_data: list[dict] = json.load(f)
                utils_logger.info('Файл считан')
            except json.JSONDecodeError:
                utils_logger.error('Ошибка в данных')
                return data
    except FileNotFoundError:
        utils_logger.error('Файл не найден')
        return data
    if type(json_data) is list:
        utils_logger.info('Ошибок нет')
        return json_data
    utils_logger.error('Ошибка формата')
    return data


# if __name__ == "__main__":
#     pathname = os.path.join(DATA_DIR, 'operations.json')
#     print(pathname)
#     print(get_transactions(pathname))
