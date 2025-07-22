import pytest


@pytest.fixture
def number_of_account_for_masks() -> str:
    return "**7890"


@pytest.fixture
def card_number_for_masks() -> str:
    return "1234 56** **** 3456"


@pytest.fixture
def number_of_account_for_widget() -> str:
    return "Счет **7890"


@pytest.fixture
def card_number_for_widget() -> str:
    return "Visa 1234 56** **** 3456"


@pytest.fixture
def data_for_test_processing() -> list:
    # Данные для проверки тестов функиций фильтрации по статсусу и сортировки по дате
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019:07:03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018+10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018,09,12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
