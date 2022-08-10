import sys
import unittest
from inthashmaps import *
from random import randint

class ar_test(unittest.TestCase):

    def test_base(self): #100 random arrays, 20 values each from 1 to 10
        for i in range(100):
            ar = list()
            for j in range(20):
                ar.append(randint(1,10))
            br = freq_ar(ar,10)
            for k in range(10):
                assert br[k] == ar.count(k+1)
                
    def test_speed(self): #array with 448 1's, 448 2's... 448 448's
        #this test takes under 0.1s, ~200000 operations
        ar = list()
        for i in range(448):
            for j in range(448):
                ar.append(i+1)
        br = freq_ar(ar,448)
        for k in range(448):
            assert br[k] == 448

#class dict_test(unittest.TestCase): #assumes freq_ar is working

    


if __name__ == "__main__":
    unittest.main()
