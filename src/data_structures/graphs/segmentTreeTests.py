import sys
import unittest
from segmentTree import *
from random import randint

class seg_test(unittest.TestCase):

    def test_speed(self):
        #n = 50000 takes over 1 second, find optimization for segmentTree.py 
        ar = list()
        n = 50000
        for i in range(n):
            ar.append(i)
        t = create_segtree(ar)
        for j in range(n):
            a,b = randint(0,n-1),randint(0,n-1)
            assert seg_search(min(a,b),max(a,b),t) == max(a,b)

if __name__ == "__main__":
    unittest.main()
