import time
from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_1 = time.time()
                result = func(*args, **kwargs)
                time_2 = time.time()
                name_func = func.__name__
                if filename:
                    file = open(filename, "w", encoding="utf-8")
                    file.write(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}\n\n")
                    file.close()
                else:
                    print(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}")
            except TypeError:
                name_func = func.__name__
                if filename:
                    file = open(filename, "w", encoding="utf-8")
                    file.write(f"{name_func} error: TypeError. Inputs: {args}, {kwargs}")
                    file.close()
                else:
                    print(f"{name_func} error: TypeError. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


# @log(filename="2.txt")
# def summa(a, b):
#     """Сумма двух чисел"""
#     return a + b
#
#
# summa("2", 3)
