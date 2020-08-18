import pytest
import time


def func(x):
    return x + 1


@pytest.mark.parametrize("values, result", [(1, 2), (2, 3), (3, 4)])
def test_add_one(values, result):
    time.sleep(3)
    assert func(values) == result
