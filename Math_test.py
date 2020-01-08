import pytest

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = NUMBER_1 + NUMBER_2
    assert value == 5.0