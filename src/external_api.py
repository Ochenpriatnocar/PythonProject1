import os

import requests
from dotenv import load_dotenv


def transactions_by_rub(operation: dict) -> float | None:
    """Функция конвертации транзакции в рубли"""

    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": f"{API_KEY}"}

    if operation["operationAmount"]["currency"]["code"] == "RUB":
        return float(operation["operationAmount"]["amount"])

    elif (
        operation["operationAmount"]["currency"]["code"] == "EUR"
        or operation["operationAmount"]["currency"]["code"] == "USD"
    ):
        payload = {
            "to": "RUB",
            "from": {operation["operationAmount"]["currency"]["code"]},
            "amount": {operation["operationAmount"]["amount"]},
        }
        response_json = requests.get(url, headers=headers, params=payload)
        status_code = response_json.status_code
        if status_code == 200:
            return round(float(response_json.json()["result"]), 2)
        elif status_code == 404:
            print("Неверный запрос")
        else:
            status_code == 500
            print("Непредвиденная ошибка на сервере")
    return
