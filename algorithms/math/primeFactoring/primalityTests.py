import sys
import unittest
from primality import * 
from sieveOfEratosthenes import *
from random import randint
class prime_test(unittest.TestCase):
    
    def test_base(self): #check if accurate up to 10^5, check against sieve
        note: with 100000 calls to the function and each call taking O((log n)^3)
        time, this test is expected to take a few seconds.
        n = 100000
        s = sieve(n)
        for i in range(n+1):
            assert prime(i) == s[i]
    
    def test_rspeed(self): #test speed with random values
        #only starts slows down noticably around 10**200ish
        n = 10**200
        for i in range(100):
            prime(randint(1,n))

    


if __name__ == "__main__":
    unittest.main()
