import logging
import os.path

from config import LOGS_DIR

masks_logger = logging.getLogger(__name__)
masks_logger.setLevel(logging.DEBUG)
masks_path = os.path.join(LOGS_DIR, 'masks.log')
file_hendler = logging.FileHandler(masks_path, mode="w", encoding='utf-8')
file_formater = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_hendler.setFormatter(file_formater)
masks_logger.addHandler(file_hendler)


def get_mask_card_number(card_number: int = 0) -> str:
    """Функция возвращения маски по номеру  карты"""
    masks_logger.info('Вызов функции маски карты: get_mask_card_number')
    card_number_str = str(card_number).zfill(16)
    if type(card_number) is int and len(str(card_number)) <= 16:
        mask_number = card_number_str[0:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
        masks_logger.info('Функция возвратила маску карты')
        return mask_number
    masks_logger.error(f'Ошибка в данных карты: <{card_number}>')
    return 'Неверно введены данные'


def get_mask_account(account: int = 0) -> str:
    """Функция возвращает маску счета"""
    masks_logger.info('Вызов функции маски счета: get_mask_account')
    if type(account) is int and len(str(account)) <= 20:
        mask_account = "**" + str(account).zfill(20)[-4:]
        masks_logger.info('Функция возвратила маску счета')
        return mask_account
    masks_logger.error(f'Ошибка в данных счета: <{account}>')
    return 'Неверно введены данные'


# if __name__ == "__main__":
#     retro = 64487911112386
#    print(get_mask_card_number(retro))
   # print(get_mask_account(12345678901234567890))
