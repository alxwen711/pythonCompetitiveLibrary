#WIP
"""
Author: Alex Wen
Last updated: August 22nd, 2022

Algorithms for factoring numbers using Pollard's rho algorithm.
Runtime for finding a factor is about O(x**0.5), where x is the
smallest factor remaining. Realistically the algorithm should be
usable until 10^12.


factorize returns factors in 2d array, each array is [factor, freq]
"""
from math import gcd

def fact_func(x: int, r: int) -> int:
    return (x*x+1) % r


def find_factor(n: int) -> int:
    x = 2
    y = 2
    #i = 0
    a = 1
    while True: #unsure how many iterations are needed here
        #i += 1
        x = fact_func(x,n)
        y = fact_func(fact_func(y,n),n)
        a = gcd(n,abs(x-y))
        if a != 1:
            break
        if x == y:
            break
    #print(i)
    return a

def factorize(n: int) -> list[list[int]]:
    return None









if __name__ == "__main__":
    print(find_factor(1497631652873))
