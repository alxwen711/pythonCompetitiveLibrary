import unittest
from factorization import *
from random import randint

#needed for verification
from primality import * 
from sieveOfEratosthenes import *

class factor_test(unittest.TestCase):
    
    def test_basic(self): #test for 0 to 10000
        s = sieve(10000) #100% prime/comp acc
        for i in range(10001):
            #test i
            ar = factorize(i)
            x = 1
            for j in range(len(ar)):
                factor = ar[j][0]
                if factor > 1: assert s[ar[j][0]]
                x *= (ar[j][0] ** ar[j][1])
            assert x == i

    def test_random(self): #random values up to 10^10
        for i in range(100):
            v = randint(0,10**10)
            ar = factorize(v)
            x = 1
            for j in range(len(ar)):
                factor = ar[j][0]
                if factor > 1:
                    if not prime(ar[j][0]): #1/4^100 chance this is wrong
                        print("test failed on",v)
                        self.fail(ar[j][0],"is not prime")
                x *= (ar[j][0] ** ar[j][1])
            assert x == v

    



if __name__ == "__main__":
    unittest.main()
