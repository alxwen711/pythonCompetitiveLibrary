#WIP
"""
Author: Alex Wen
Last updated: August 22nd, 2022

Algorithms for factoring numbers using Pollard's rho algorithm

factorize returns factors in 2d array, each array is [factor, freq]
"""
from math import gcd

def fact_func(x: int, r: int) -> int:
    return (x*x+1) % r


def find_factor(n: int) -> int:
    x = 2
    y = 2
    while True: #unsure how many iterations are needed here
        x = fact_func(x,n)
        y = fact_func(fact_func(y,n),n)
        a = gcd(n,abs(x-y))
        if a != 1: return a

def factorize(n: int) -> list[list[int]]:
    return None









if __name__ == "__main__":
    print(find_factor(2759677))
