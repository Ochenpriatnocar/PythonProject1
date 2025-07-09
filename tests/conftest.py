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
