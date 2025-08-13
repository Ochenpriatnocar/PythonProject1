import json

from log_config import setup_loger

logger = setup_loger("utils", "utils.log")


def open_file(link_to_file: str) -> list:
    """Функция чтения json файла и записи данных в список"""

    logger.info("Начало работы функции")
    try:
        with open(link_to_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Получение результата функции")
        return data if data else []

    except FileNotFoundError:
        logger.info(f"Ошибка расположения файла {link_to_file}")
        return []

    except TypeError:
        logger.info("Ошибка типа данных")
        return []


if __name__ == "__main__":
    open_file("../data/operations.json")
