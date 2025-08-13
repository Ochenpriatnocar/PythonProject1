import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_account() -> None:
    """Проверка на правильность маскировки счета"""
    assert get_mask_account("12345678901234567890") == "**7890"


def test_get_mask_card_number() -> None:
    """Проверка на правильность маскировки номера карты"""
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


@pytest.mark.parametrize("account_number", ["0" * 19, "0" * 21], ids=["too short", "too long"])
def test_get_mask_account_number_of_symbols(account_number: str) -> None:
    """Проверка обработки исключений по длине счета"""
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр"):
        get_mask_account(account_number)


def test_get_mask_account_symbols_correctness() -> None:
    """Проверка обработки исключени корректности счета"""
    with pytest.raises(ValueError, match="Номер счета должен содержать только цифры"):
        get_mask_account("1234567890123456789n")


@pytest.mark.parametrize("card_number", ["0" * 15, "0" * 17], ids=["too short", "too long"])
def test_get_mask_card_number_number_of_symbols(card_number: str) -> None:
    """Проверка обработки исключений по длине номера карты"""
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number(card_number)


def test_get_mask_card_number_symbols_correctness() -> None:
    """Проверка обработки исключений корректности номера карты"""
    with pytest.raises(ValueError, match="Номер карты должен содержать только цифры"):
        get_mask_card_number("12345678901234nn")
