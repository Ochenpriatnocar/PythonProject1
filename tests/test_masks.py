import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_account(number_of_account_t: str) -> None:
    assert get_mask_account("12345678901234567890") == number_of_account_t


def test_get_mask_card_number(card_number_t: str) -> None:
    assert get_mask_card_number("1234567890123456") == card_number_t


def test_get_mask_account_number_of_symbols() -> None:
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр"):
        get_mask_account("1234567890123456789")


def test_get_mask_account_symbols_correctness() -> None:
    with pytest.raises(ValueError, match="Номер счета должен содержать только цифры"):
        get_mask_account("1234567890123456789n")


def test_get_mask_card_number_number_of_symbols() -> None:
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("")


def test_get_mask_card_number_symbols_correctness() -> None:
    with pytest.raises(ValueError, match="Номер карты должен содержать только цифры"):
        get_mask_card_number("12345678901234nn")
