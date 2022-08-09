import unittest
from random import randint


#binarySearch.py copied here to demonstrate bfunc modularity
def bfunc(x: int, ar = None) -> bool:
    #this function is edited for use case
    if x**2 >= ar: return True
    return False

def bsearch(low: int, high: int, ar = None) -> int:
    while high - low > 1:
        mid = (low+high)//2
        if bfunc(mid,ar): high = mid
        else: low = mid

    #diff between high and low is 1 (or 0)
    if bfunc(high,ar): return high
    else: return low


class algorithm_test(unittest.TestCase):

    def test_square(self):
        #example use with a trivial problem
        #given a square number, determine its square root (no using **.5/sqrt)
        #note that log(100000000,base=2) is about 26.5, O(26.5n) may be a factor
        #in problems with a 1 second time limit
        for i in range(100000):
            v = randint(1,100000000) #value to guess
            self.assertEqual(bsearch(1,100000000,v**2),v)

if __name__ == "__main__":
    unittest.main()
