#WIP
"""
Author: Alex Wen
Last updated: August 22nd, 2022

Sieve of Eratosthenes implementation for finding all primes up to n.
Runtime is O(n log log n), which is close enough to O(n) for most uses.
"""
from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(2,n//i+1):
                ar[i*j] = False
    return ar



if __name__ == "__main__":
    print(sieve(20))
