import sys
import unittest
from primality import * 
from sieveOfEratosthenes import *

class prime_test(unittest.TestCase):

    def test_base(self): #check if accurate up to 10^5, check against sieve
        """
        note: with 100000 calls to the function and each call taking O((log n)^3)
        time, this test is expected to take a few seconds.
        """
        n = 100000
        s = sieve(n)
        for i in range(n+1):
            assert prime(i) == s[i]

    
        


if __name__ == "__main__":
    unittest.main()
