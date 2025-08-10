import os

import requests
from dotenv import load_dotenv

# from src.utils import open_file


def transactions_by_rub(operation):
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
        return round(float(response_json.json()["result"]), 2)
    return


# data_str = open_file('../data/operations.json')
# a = transactions_by_rub(data_str[1])
# print(a)
