import os
import sys
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.math.eratosthenes import * 

#Example use can be found in exampleuses/230b.py

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def test_acc(): #test 0 to 100
    x = sieve(100)
    s = sieve(100)
    for i in range(101):
        if primes.count(i) == 0: assert s[i] == False
        else: assert s[i] == True
    
def test_speed(): #run sieve for 0 to 1000000, should be sub 1 second
    x = sieve(1000000)
    assert sum(x) == 78498


def test_acc(): 
    x = fsieve(100)
    for i in range(2,101):
        factors = list() #contains prime factors (12 -> [2,2,3])
        n = i
        while True:
            j = x[n]
            if j == 0: pytest.fail("0 val illegally detected")
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
    
def test_speed(): # run fsieve for 0 to 1000000, should be sub 1 second
    x = fsieve(1000000)
    assert x.count(1) == 78498
    for p in primes:
        assert x[p*p] == p