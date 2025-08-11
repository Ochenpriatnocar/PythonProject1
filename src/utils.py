import json


def open_file(link_to_file: str) -> list:
    """Функция чтения json файла и записи данных в список"""
    try:
        with open(link_to_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if data else []
    except FileNotFoundError:
        return []
    except TypeError:
        return []
