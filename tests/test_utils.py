import json
import os
from unittest.mock import Mock

import pytest

from src.utils import open_file


def test_open_file_with_mock():
    """Тестирование с помощью заглушки Моск"""
    mock_open_file = Mock(
        return_value={
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
    open_file = mock_open_file
    assert open_file() == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_open_file.assert_called_once()


def test_open_file(data_operations):
    """Тестирование работы функции открытия файла"""
    assert open_file("../data/operations.json") == data_operations


def test_open_file_note_found():
    """Тестирование работы функции открытия файла"""
    assert open_file("../data/operations1.json") == []


def test_open_file_type_error():
    """Тестирование работы по ошибке типа"""
    mock_open_file = {}
    assert open_file(mock_open_file) == []
