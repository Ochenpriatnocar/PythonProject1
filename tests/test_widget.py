import pytest

from src.widget import get_date
from src.widget import mask_account_card


def test_mask_account_card_for_account(number_of_account_for_widget: str) -> None:
    # Проверка на правильность обработки маскировки счета
    assert mask_account_card("Счет 12345678901234567890") == number_of_account_for_widget


def test_mask_account_card_for_card_number(card_number_for_widget: str) -> None:
    # Проверка на правильность обработки маскировки номера карты
    assert mask_account_card("Visa 1234567890123456") == card_number_for_widget


@pytest.mark.parametrize(
    "some_string, some_result",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ],
)
def test_mask_account_card(some_string: str, some_result: str) -> None:
    # Проверка на правильность выбора счета или платежной системы и корректной маскировки
    assert mask_account_card(some_string) == some_result


def test_get_mask_account_number_of_symbols() -> None:
    # Проверка на длинну номера счета
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр"):
        mask_account_card("Счет 1234567890123456789")


def test_get_mask_account_symbols_correctness() -> None:
    # Проверка на корректность номера счета
    with pytest.raises(ValueError, match="Номер счета должен содержать только цифры"):
        mask_account_card("счёт 1234567890123456789n")


@pytest.mark.parametrize(
    "date_in_string, date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024+03+11T02:26:18.671407", "11.03.2024"),
        ("2024:03:11T02:26:18.671407", "11.03.2024"),
        ("2024;03;11T02:26:18.671407", "11.03.2024"),
        ("2024.03,11T02:26:18.671407", "11.03.2024"),
    ],
)
def test_get_date(date_in_string: str, date: str) -> None:
    # Проверка правильности обработки данных при разных форматах даты
    assert get_date(date_in_string) == date


def test_get_date_correct_date() -> None:
    # Проверка на вхождение строки без даты
    with pytest.raises(ValueError, match="Не корректная дата"):
        get_date("2024-03T02:26:18.671407")
