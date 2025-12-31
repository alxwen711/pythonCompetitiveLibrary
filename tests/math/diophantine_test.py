import os
import sys
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


from src.math.diophantine import *

def test_basic():
    a, b, c = 3, 5, 2
    x, y, v, w = dio(a, b, c)
    assert a * x + b * y == c


def test_no_solution():
    assert dio(4, 6, 3) == (-1, -1, -1, -1)


def test_zero_a():
    x, y, v, w = dio(0, 5, 10)
    assert 0 * x + 5 * y == 10


def test_zero_b():
    x, y, v, w = dio(7, 0, 21)
    assert 7 * x + 0 * y == 21


def test_both_zero():
    x, y, v, w = dio(0, 0, 0)
    assert x == 0 and y == 0


def test_general_solution():
    a, b, c = 6, 9, 3
    x, y, v, w = dio(a, b, c)
    assert a * x + b * y == c
    assert a * (x + v) + b * (y - w) == c


