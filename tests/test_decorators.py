from typing import Any

import pytest

from src.decorators import f_name, log_file, log_ok, v_error, v_error_file


def test_log_err() -> None:
    with pytest.raises(Exception, match="error: Что то пошло не так!"):
        v_error()


def test_log_err_file() -> None:
    # with pytest.raises(Exception, match="error: Что то пошло не так!"):
    v_error_file()
    with open('proba.txt', "r") as f:
        content = f.readlines()
        assert content[-1] == "v_error_file error: Something went wrong!. Inputs: (), {}\n"


def test_log_file_err(capsys: Any) -> None:
    '''Тест на ошибку ввода в имени файла'''
    f_name()
    captured = capsys.readouterr()
    assert captured.out == "f_name error: [Errno 22] Invalid argument: '>>>.txt'. Inputs: (), {}\n"


def test_log_ok(capsys: Any) -> None:
    log_ok(1, 10)
    captured = capsys.readouterr()
    assert captured.out == "log_ok, Inputs: (1, 10), {} Result: 0.1 - ok\n"
    assert captured.err == ""


def test_log_to_file() -> None:
    log_file(20, 10)
    # filename = 'proba.txt'
    with open('proba.txt', "r") as f:
        content = f.readlines()
        assert content[-1] == "log_file, Inputs: (20, 10), {} Result: 2.0 - ok\n"
