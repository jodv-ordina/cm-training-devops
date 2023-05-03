import pytest

from math_api.math.fibonacci import fibonacci, fibonacci_cached


def test_fib_negative():
    with pytest.raises(ValueError):
        fibonacci(-9999)


# def test_fib_small():
#     assert fibonacci(3) == 2


def test_fib_cached_negative():
    with pytest.raises(ValueError):
        fibonacci_cached(-9999)


def test_fib_cached_small():
    assert fibonacci_cached(3) == 3


# test is timed out after 5 seconds
@pytest.mark.timeout(5)
def test_fib_cached_large():
    assert fibonacci_cached(100) == 573147844013817084101
