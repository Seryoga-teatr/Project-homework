from functools import wraps


def log(filename=''):
    '''Декоратор для логирования результов и ошибок в консоль или в файл'''
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if filename == '':
                try:
                    result = func(*args, **kwargs)
                    print(f'{func.__name__}, Inputs: {args}, {kwargs} Result: {result} - ok')
                    return result
                except Exception as e:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            else:
                try:
                    with open(filename, "a") as file:
                        try:
                            result = func(*args, **kwargs)
                            file.write(f'{func.__name__}, Inputs: {args}, {kwargs} Result: {result} - ok\n')
                            return result
                        except Exception as e:
                            file.write(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n')
                except Exception as e:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')

            return
        return wrapper
    return inner


@log('proba.txt')
def mini(x=5, y=1):
    return x / y

mini()
