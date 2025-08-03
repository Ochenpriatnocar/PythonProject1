import time
from functools import wraps


def log(filename=None):
    """Декоратор логирования"""
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            try:
                time_1 = time.time()
                result = func(*args, **kwargs)
                time_2 = time.time()
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}\n\n")
                    file.close()
                else:
                    print(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}")
                return result
            except TypeError:
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"{name_func} error: TypeError. Inputs: {args}, {kwargs}\n")
                    file.close()
                else:
                    print(f"{name_func} error: TypeError. Inputs: {args}, {kwargs}")

        return decorator

    return wrapper


# @log()
# def summa(a, b):
#     """Сумма двух чисел"""
#     return a + b
#
#
# data = summa(3, 4)
# print(help(summa))

