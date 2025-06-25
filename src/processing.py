# from src.widget import get_date


def filter_by_state(list_of_status_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации по статусу операции"""

    operation_executed = []
    operation_canceled = []

    for operation in list_of_status_state:
        if operation["state"] == "EXECUTED":
            operation_executed.append(operation)
        elif operation["state"] == "CANCELED":
            operation_canceled.append(operation)
    if state == "EXECUTED":
        return operation_executed
    elif state == "CANCELED":
        return operation_canceled
