"""
Author: Alex Wen
Last updated: August 26th, 2022

Sieve of Eratosthenes implementation for finding all primes up to n.
Runtime is O(n log log n), which is close enough to O(n) for practical use.

sieve(n)
Returns an array with n+1 elements. If A[x] == True, x is prime,
else x is composite.

fsieve(n)
Returns an array with n+1 elements. If A[x] == 1, x is prime,
else x's smallest prime factor is stored (useful for prime factorization).
Note that A[0] and A[1] will always equal 0 as they are not prime.
"""
from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    return ar

def fsieve(n: int) -> list[int]: 
    ar = [1]*max(2,(n+1))
    ar[0] = 0
    ar[1] = 0
    for i in range(2,floor(sqrt(n))+1):
        if ar[i] == 1: #i is prime
            for j in range(i,n//i+1):
                if ar[i*j] == 1: ar[i*j] = i
    return ar

if __name__ == "__main__":
    print(fsieve(20))
