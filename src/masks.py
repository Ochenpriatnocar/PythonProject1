def get_mask_account(account_of_card: str) -> str:
    """Маскировка с 1 по 16 символов номера счета карты"""

    if len(account_of_card) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    if not account_of_card.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")
    return "**" + account_of_card[-4:]


def get_mask_card_number(number_of_card: str) -> str:
    """Маскировка с 7 по 12 символов номера карты"""

    if len(number_of_card) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    if not number_of_card.isdigit:
        raise ValueError("Номер карты должен содержать только цифры")
    return number_of_card[0:4] + " " + number_of_card[4:6] + "** " + "****" + " " + number_of_card[12:]
