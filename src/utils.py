import json
from log_config import setup_loger

logger = setup_loger("utils", "utils.log")

def open_file(link_to_file: str) -> list:
    """Функция чтения json файла и записи данных в список"""
    try:
        with open(link_to_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.debug(f"Старт")
        return data if data else []
    except FileNotFoundError:
        return []
    except TypeError:
        return []

if __name__ == "__main__":
    open_file("../data/operations.json")