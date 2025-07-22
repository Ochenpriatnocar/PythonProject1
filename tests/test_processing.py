import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize(
    "state, count",
    [
        ("CANCELED", 2),
        ("EXECUTED", 2),
        ("", 2),
    ],
)
def test_filter_by_state(data_for_test_processing: list[dict], state: str, count: int) -> None:
    # Тестирование функии фильтрации операций по статусу, и с отсутствующим статусом
    result = filter_by_state(data_for_test_processing, state)
    assert len(result) == count


def test_filter_by_invalid_state(data_for_test_processing: list) -> None:
    # Тестирование функии фильтрации операций по статусу при отсутствии словарей с указанным статусом
    with pytest.raises(ValueError, match="Указанного статуса нет в списке"):
        filter_by_state(data_for_test_processing, "INVALID")


@pytest.mark.parametrize(
    "reverse_status, result",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(data_for_test_processing: list, reverse_status: bool, result: list) -> None:
    # Тестирование функции сортировки по дате в зависимости от статуса сортировки, и корректности даты
    assert sort_by_date(data_for_test_processing, reverse_status) == result
