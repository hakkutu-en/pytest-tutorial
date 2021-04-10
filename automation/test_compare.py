import py
from pytest import mark
import pytest

@pytest.mark.xfail
@mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.xfail
@mark.great
def test_greater_equal():
    num  = 100
    assert num >= 100

@pytest.mark.skip
@mark.others
def test_less():
    num = 100
    assert num < 200