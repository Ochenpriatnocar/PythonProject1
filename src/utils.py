import json


def open_file(link_to_file) -> list:
    """ Функция чтения json файла и записи данных в словарь"""
    try:
        with open(link_to_file, encoding='utf-8') as f:
            data = json.load(f)
        return data
    except:
        return []


# data_str = open_file('../data/operations.json')
# print(data_str)
# print(type(data_str))
#
# for x in data_str:
#     if x == {}:
#         continue
#     else:
#         print(x["operationAmount"]["amount"])
