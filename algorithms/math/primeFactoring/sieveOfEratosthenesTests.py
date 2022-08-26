import sys
import unittest
from sieveOfEratosthenes import * #change to filename


class sieve_test(unittest.TestCase):

    def test_acc(self): #test 0 to 100
        x = sieve(100)
        s = sieve(100)
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        for i in range(101):
            if primes.count(i) == 0: assert s[i] == False
            else: assert s[i] == True
        
    def test_speed(self): #run sieve for 0 to 1000000, should be sub 1 second
        x = sieve(1000000)
        assert sum(x) == 78498

class fsieve_test(unittest.TestCase):

    def test_acc(self): #fsieve usage in prime factorization
        x = fsieve(100)
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        for i in range(2,101):
            factors = list() #contains prime factors (12 -> [2,2,3])
            n = i
            while True:
                j = x[n]
                if j == 0: self.fail("0 val illegally detected")
                elif j == 1:
                    factors.append(n)
                    break
                else:
                    factors.append(j)
                    assert n % j == 0
                    n = n // j
            s = 1
            for k in range(len(factors)):
                assert primes.count(factors[k]) == 1
                s *= factors[k]
            assert s == i
        
    def test_speed(self):
        x = sieve(1000000)
        assert x.count(1) == 78498
        

if __name__ == "__main__":
    unittest.main()
