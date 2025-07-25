import re

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция маскировки номера карты или счета"""

    account_or_paiment_sistem, account_or_card_number = account_info.rsplit(" ", maxsplit=1)

    if account_or_paiment_sistem.lower() == "счет" or account_or_paiment_sistem.lower() == "счёт":
        return account_or_paiment_sistem + " " + get_mask_account(account_or_card_number)
    else:
        return account_or_paiment_sistem + " " + get_mask_card_number(account_or_card_number)


def get_date(string_date: str) -> str | None:
    """Преобразование даты в читаемый формат"""

    date_, time_ = string_date.rsplit("T")

    if len(date_) != 10:
        raise ValueError("Не корректная дата")

    correct_date_ = re.split(r"[-+.,;: ]+", date_)[::-1]
    return ".".join(correct_date_)
