from automation import __version__
from automation.automation import numbers, email


def test_version():
    assert __version__ == '0.1.0'


def test_numbers():
    actual = numbers()
    excepted = open("phone_numbers.txt", "r").read()
    assert actual == excepted


def test_email():
    actual = email()
    excepted = open("emails.txt", "r").read()
    assert actual == excepted
