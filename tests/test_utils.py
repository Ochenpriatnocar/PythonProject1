from unittest.mock import Mock

from config import ROOT_DIR
from src.utils import open_file


def test_open_file_with_mock(data_operations: list) -> None:
    """Тестирование с помощью заглушки Моск"""
    mock_open_file = Mock(return_value=data_operations[1])
    open_file = mock_open_file
    assert open_file(mock_open_file) == data_operations[1]
    mock_open_file.assert_called_once()


def test_open_file(data_operations: list) -> None:
    """Тестирование работы функции открытия файла"""

    # tests_dir = os.path.dirname(__file__)
    assert open_file(f"{ROOT_DIR}/data/operations.json") == data_operations
    # target_file = os.path.join(tests_dir, '..', 'data', 'operations.json')
    # assert open_file(target_file) == data_operations


def test_open_file_note_found() -> None:
    """Тестирование работы функции открытия при отсутствии файла"""
    assert open_file("../data/operations1.json") == []


def test_open_file_type_error() -> None:
    """Тестирование работы по ошибке типа"""
    assert open_file({}) == []
