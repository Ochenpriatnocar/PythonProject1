import re


def filter_by_state(transactions: list, state: str = "EXECUTED") -> list | None:
    """Функция фильтрации по статусу операции"""

    transactions_executed = []
    transactions_canceled = []

    for transaction in transactions:
        if transaction["state"] == "EXECUTED":
            transactions_executed.append(transaction)
        elif transaction["state"] == "CANCELED":
            transactions_canceled.append(transaction)
    if state == "CANCELED":
        return transactions_canceled
    elif state == "EXECUTED" or state == "":
        return transactions_executed
    else:
        raise ValueError("Указанного статуса нет в списке")


def sort_by_date(list_of_date: list[dict], reverse_: bool = True) -> list[dict]:
    """Функция сортировки элементов списка по дате"""

    for dict_ in list_of_date:
        for key, value in dict_.items():

            if key == "date":
                date_, time_ = value.rsplit("T")
                correct_value = re.split(r"[-+.,;: ]+", date_)
                string_correct_value = "-".join(correct_value)
                dict_.update({"date": string_correct_value + "T" + time_})

    return sorted(list_of_date, key=lambda date: date["date"], reverse=reverse_)
