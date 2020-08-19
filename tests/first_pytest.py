import pytest
import time


def add_one(x):
    return x + 1


def minus_one(x):
    return x - 1


def kali_two(x):
    return x * 2


def bagi_two(x):
    return x / 2


@pytest.mark.parametrize("values, result", [(1, 2), (2, 3), (3, 4)])
@pytest.mark.add
@pytest.mark.math
def test_add_one(values, result):
    time.sleep(3)
    assert add_one(values) == result


@pytest.mark.parametrize("values, result", [(2, 1), (3, 2), (4, 3)])
@pytest.mark.minus
@pytest.mark.math
def test_minus_one(values, result):
    time.sleep(3)
    assert minus_one(values) == result


@pytest.mark.parametrize("values, result", [(1, 2), (2, 4), (3, 6)])
@pytest.mark.kali
@pytest.mark.math
def test_kali_two(values, result):
    time.sleep(3)
    assert kali_two(values) == result


@pytest.mark.parametrize("values, result", [(2, 1), (4, 2), (6, 3)])
@pytest.mark.bagi
@pytest.mark.math
def test_bagi_two(values, result):
    time.sleep(3)
    assert bagi_two(values) == result
