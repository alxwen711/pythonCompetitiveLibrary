import unittest
from convexPolygonArea import *

class integration_test(unittest.TestCase):

    def test_triangle(self):
        triangle = [[0,-2],[4,0],[2,4]] #area is 10
        error = abs(heron_area(triangle)-10)
        assert error < 0.00000001


    def test_polygon(self):
        polygon = [[0,-1],[3,1],[5,3],[1,2],[-1,1]] #area is 9
        error = abs(heron_area(polygon)-9)
        assert error < 0.00000001


class unit_test(unittest.TestCase):

    def test_py(self): #classic 3-4-5 side length triangle
        error = abs(pythagoras([0,3],[4,0])-5)
        assert error < 0.00000001

    def test_py(self): #area of equilateral triangle with side length 3
        error = abs(heron_triangle(3,3,3)-3.897114317029974)
        assert error < 0.00000001

    


if __name__ == "__main__":
    unittest.main()
