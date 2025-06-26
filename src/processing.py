def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Функция фильтрации по статусу операции"""

    transactions_executed = []
    transactions_canceled = []

    for transaction in transactions:
        if transaction["state"] == "EXECUTED":
            transactions_executed.append(transaction)
        elif transaction["state"] == "CANCELED":
            transactions_canceled.append(transaction)
    if state == "EXECUTED":
        return transactions_executed
    elif state == "CANCELED":
        return transactions_canceled


def sort_by_date(list_of_date: list[dict], reverse_: bool = True) -> list[dict]:
    """Функция сортировки элементов списка по дате"""

    sorted_list_of_date = sorted(list_of_date, key=lambda date: date["date"], reverse=reverse_)
    return sorted_list_of_date
