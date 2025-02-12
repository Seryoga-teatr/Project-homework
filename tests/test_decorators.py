import pytest
from src.decorators import v_error, f_name, log_ok


def test_log_err():
    with pytest.raises(Exception, match="error: Что то пошло не так!"):
        v_error()


def test_log_file():
    with pytest.raises(Exception, match="Invalid filename!"):
        f_name()


def test_log_ok(capsys):
    log_ok(1, 10)
    captured = capsys.readouterr()
    assert captured.out == "log_ok, Inputs: (1, 10), {} Result: 0.1 - ok\n"
    assert captured.err == ""

