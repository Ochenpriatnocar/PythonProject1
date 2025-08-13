from log_config import setup_loger

logger = setup_loger("masks", "masks.log")


def get_mask_account(account_of_card: str) -> str:
    """Маскировка с 1 по 16 символов номера счета карты"""

    logger.info("Начало работы функции get_mask_account")
    if len(account_of_card) != 20:

        logger.error("Ошибка данных, счет 20 цифр")
        raise ValueError("Номер счета должен содержать 20 цифр")

    if not account_of_card.isdigit():
        logger.error("Ошибка данных, только цифры")
        raise ValueError("Номер счета должен содержать только цифры")

    logger.info("Получение результата вывода функции get_mask_account")
    return "**" + account_of_card[-4:]


def get_mask_card_number(number_of_card: str) -> str:
    """Маскировка с 7 по 12 символов номера карты"""

    logger.info("Начало работы функции get_mask_card_number")
    if len(number_of_card) != 16:

        logger.error("Ошибка данных, счет 16 цифр")
        raise ValueError("Номер карты должен содержать 16 цифр")

    if not number_of_card.isdigit():
        logger.error("Ошибка данных, только цифры")
        raise ValueError("Номер карты должен содержать только цифры")

    logger.info("Получение результата вывода функции get_mask_card_number")
    return number_of_card[0:4] + " " + number_of_card[4:6] + "** **** " + number_of_card[12:]
