import os
import sys
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from src.algorithms.convexPolygonArea import *


def test_triangle():
    triangle = [[0,-2],[4,0],[2,4]] #area is 10
    error = abs(heron_area(triangle)-10)
    assert error < 0.00000001


def test_polygon():
    polygon = [[0,-1],[3,1],[5,3],[1,2],[-1,1]] #area is 9
    error = abs(heron_area(polygon)-9)
    assert error < 0.00000001


def test_pythag(): #classic 3-4-5 side length triangle
    error = abs(pythagoras([0,3],[4,0])-5)
    assert error < 0.00000001

def test_equi(): #area of equilateral triangle with side length 3
    error = abs(heron_triangle(3,3,3)-3.897114317029974)
    assert error < 0.00000001

    


