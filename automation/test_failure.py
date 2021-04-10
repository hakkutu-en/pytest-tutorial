import pytest
from math import sqrt

def test_sqrt_failure():
    num = 25
    assert sqrt(num) == 6

def test_square_failure():
    num = 7
    assert num * num == 40

def test_equality_failure():
    assert 10 == 11