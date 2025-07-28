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
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result} \nКонец: {time_2}\n\n")
                    file.close()
                else:
                    print(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result} \nКонец: {time_2}")
            except Exception as e:
                print(f"Начало: {time_1}\n{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n{time_2}")

        return wrapper

    return decorator


# @log()
# def summa(a, b):
#     return a + b
#
#
# summa(2, 3)
