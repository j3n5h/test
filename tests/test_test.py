from src.test import test
from src import __version__


def test_version() -> None:
    assert __version__ == '0.1.1'


def test_test() -> None:
    assert test() == 'Hello World!'
