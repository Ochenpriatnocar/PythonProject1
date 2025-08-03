import pytest

from src.decorators import log


def test_log_file():
    """Проверка корректности ведения записи в лог файл"""

    @log(filename="1.txt")
    def summa(x, y):
        return x + y

    summa(1, 2)
    with open("1.txt", "r", encoding="utf-8") as file:
        assert file.readlines()[-3] == "Функция summa ок. Результат: 3\n"


def test_log(capsys):
    """Проверка корректности записи в консоли"""

    @log()
    def summa(x, y):
        return x + y

    summa(1, 2)
    captured = capsys.readouterr()
    assert captured.out[captured.out.find("Ф") : captured.out.find("К")] == "Функция summa ок. Результат: 3\n"


def test_error_log_file():
    """Проверка корректности ведения записи об ошибке в лог файл"""

    @log(filename="1.txt")
    def summa(x, y):
        return x + y

    summa("1", 2)
    with open("1.txt", "r", encoding="utf-8") as file:
        assert file.readlines()[-1] == "summa error: TypeError. Inputs: ('1', 2), {}\n"


def test_error_log(capsys):
    """Проверка корректности записи об ошибке в консоли"""

    @log()
    def summa(x, y):
        return x + y

    summa("1", 2)
    captured = capsys.readouterr()
    assert captured.out[:-1] == "summa error: TypeError. Inputs: ('1', 2), {}"
