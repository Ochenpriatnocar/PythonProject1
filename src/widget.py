from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция маскировки номера карты или счета"""

    account_or_paiment_sistem, account_or_card_number = account_info.rsplit(" ", maxsplit=1)

    if account_or_paiment_sistem.lower() == "счет" or account_or_paiment_sistem.lower() == "счёт":
        return account_or_paiment_sistem + " " + get_mask_account(account_or_card_number)
    else:
        return account_or_paiment_sistem + " " + get_mask_card_number(account_or_card_number)


def get_date(string_date: str) -> str:
    """Преобразование даты в читаемый формат"""

    return str(string_date[8:10] + "." + string_date[5:7] + "." + string_date[0:4])
