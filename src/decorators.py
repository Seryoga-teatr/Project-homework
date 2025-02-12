from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str = '') -> Callable[..., Any]:
    '''Декоратор для логирования результов и ошибок в консоль или в файл'''
    def inner(func):
        '''Внутренняя функция'''
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict):
            '''Функция - обертка'''
            if filename == '':
                try:
                    result = func(*args, **kwargs)
                    print(f'{func.__name__}, Inputs: {args}, {kwargs} Result: {result} - ok')
                    return result
                except Exception as e:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                    raise Exception(f"error: {e}")
            else:
                try:
                    with open(filename, "a") as file:
                        try:
                            result = func(*args, **kwargs)
                            file.write(f'{func.__name__}, Inputs: {args}, {kwargs} Result: {result} - ok\n')
                            return result
                        except Exception as e:
                            file.write(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n')
                            raise Exception(f"error: {e}")
                except Exception as e:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                    raise Exception(f"error: {e}")
        return wrapper
    return inner


@log('')
def log_ok(x: int = 5, y: int = 1) -> float:
    '''Штатный тест'''
    return x / y


@log('')
def v_error() -> None:
    '''Тест на ошибку данных'''
    raise ValueError("Что то пошло не так!")


@log('')
def f_name() -> None:
    '''Тест на ошибку в имени файла'''
    raise OSError("Invalid filename!")


# print(log_ok(1, 5))
