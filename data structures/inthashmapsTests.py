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

class dict_test(unittest.TestCase): #assumes freq_ar is working

    def test_freq(self): #test pos = False
        ar = list()
        for i in range(100000):
            ar.append(randint(1,100000))
        d = freq_dict(ar)
        test = freq_ar(ar,100000)
        for j in range(100000):
            x = test[j]
            if x == 0:
                assert d.get(j+1) == None
            else:
                assert d[j+1] == x 

    def test_pos(self): #test pos = True
        ar = list()
        for i in range(100000):
            ar.append(randint(1,100000))
        d = freq_dict(ar,True)
        correct = 0
        for j in range(100000):
            if d.get(j+1) != None:
                for k in range(len(d[j+1])):
                    if ar[d[j+1][k]] == j+1: correct += 1
        assert correct == 100000

    

    

if __name__ == "__main__":
    unittest.main()
