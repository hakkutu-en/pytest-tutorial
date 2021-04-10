from pytest import mark
import math

@mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@mark.square
def testsquare():
    num = 7
    assert num*num == 40

@mark.others
def test_equality():
    assert 10 == 11
