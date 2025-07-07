import pytest


@pytest.fixture
def number_of_account_t() -> str:
    return "**7890"


@pytest.fixture
def card_number_t() -> str:
    return "1234 56** **** 3456"
