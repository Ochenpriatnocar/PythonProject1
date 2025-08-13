def filter_by_currency(transactions: list[dict], currency: str = "USD"):
    """Функция фильтрации транзакций по заданной валюте"""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]):
    """функция возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        descriptions = [transaction["description"]]
        yield descriptions


def card_number_generator(start: int, stop: int):
    """Генерирует номера банковских карт."""

    for i in range(start, stop + 1):
        card_number = str(i).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
