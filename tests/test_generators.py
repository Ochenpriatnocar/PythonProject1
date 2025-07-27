import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.mark.parametrize("currency, count", [("USD", 3), ("RUB", 2), ("EUR", 0)])
def test_filter_by_currency(transactions: list[dict], currency: str, count: int) -> None:
    """Тестирование фильтрации списка по валюте, а также в случае отсутствия операция с определенной валютой (EUR)"""
    assert len(list(filter_by_currency(transactions, currency))) == count


def test_filter_by_currency_for_empty() -> None:
    """Тестирование фильтрации списка при пустом списке"""
    assert list(filter_by_currency([], "USD")) == []


@pytest.mark.parametrize(
    "count, result",
    [
        (
            5,
            [
                ["Перевод организации"],
                ["Перевод со счета на счет"],
                ["Перевод со счета на счет"],
                ["Перевод с карты на карту"],
                ["Перевод организации"],
            ],
        ),
        (
            3,
            [
                ["Перевод организации"],
                ["Перевод со счета на счет"],
                ["Перевод со счета на счет"],
            ],
        ),
        (0, []),
    ],
)
def test_transaction_descriptions(count: int, result: list[dict], transactions: list[dict]) -> None:
    """Проверка возврата правильных описаний функции"""
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[:count] == result


def test_transaction_descriptions_for_empty() -> None:
    """Проверка возврата правильных описаний функции при входе пустого списка"""
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, stop: int, result: str) -> None:
    """Тестирование генератора на корректность работы"""
    assert list(card_number_generator(start, stop)) == result
