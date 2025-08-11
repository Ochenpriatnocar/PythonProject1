from unittest.mock import Mock
from unittest.mock import patch

from src.external_api import transactions_by_rub


def test_transactions_by_rub_with_rub(data_operations: dict) -> None:
    """Тест на конвертацию транзакции с RUB"""
    assert transactions_by_rub(data_operations[0]) == 31957.58


@patch("requests.get")
def test_transactions_by_rub_with_eur(mock_get):
    """Тест на конвертацию из EUR в RUB"""
    operation = {"operationAmount": {"currency": {"code": "EUR"}, "amount": 100.0}}

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9000.0}
    mock_get.return_value = mock_response

    result = transactions_by_rub(operation)
    assert result == 9000.0
    mock_get.assert_called_once()


@patch("requests.get")
def test_transactions_by_rub_with_usd(mock_get, data_operations: dict) -> None:
    """Тест на конвертацию из USD в RUB"""

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 65000.0}
    mock_get.return_value = mock_response

    result = transactions_by_rub(data_operations[1])
    assert result == 65000.0
    mock_get.assert_called_once()


@patch("requests.get")
def test_transactions_by_rub_with_error_404(mock_get, data_operations: dict) -> None:
    """Тестирование отработки корректности статус кодов с кодом 404"""

    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = transactions_by_rub(data_operations[1])
    assert result is None
    mock_get.assert_called_once()


@patch("requests.get")
def test_transactions_by_rub_with_error_500(mock_get, data_operations: dict) -> None:
    """Тестирование отработки корректности статус кодов с кодом 500"""

    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    result = transactions_by_rub(data_operations[1])
    assert result is None
    mock_get.assert_called_once()
