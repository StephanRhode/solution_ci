import pytest
from pytest import approx
import math
from src.my_source import add_func, euclid


def test_add_one():
    assert add_func(2, 5) == 7


@pytest.mark.xfail
def test_add_fail():
    assert add_func(5, 5) == 9


def test_euclid():
    a = [0, 0, 0]
    b = [4, 4, 4]
    dist = euclid(a, b)
    assert(math.sqrt(48.) == approx(dist))
