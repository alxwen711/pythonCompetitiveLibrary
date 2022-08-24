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

def fact_func(x: int, r: int) -> int: #may need to use other c's than 1
    return (x*x+1) % r


def find_factor(n: int) -> int:
    x = 2
    y = x
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
        """
        if a == n: #invalid case, try with new parameters
        after enough attempts then prime can be called
        """
    #print(i)
    return a

def factorize(n: int) -> list[list[int]]:
    d = {}
    while n != 1:
        prev = find_factor(n)
        x = 0
        while True:
            print(n,prev)
            x = find_factor(prev)
            if x == prev:
                break
            else: prev = x
        if d.get(x) == None: d[x] = 0
        d[x] += 1
        n = n // x
    ar = list()
    k = list(d.keys())
    for i in range(len(k)):
        ar.append([k[i],d[k[i]]])
    return ar









if __name__ == "__main__":
    #print(find_factor(1497631652873))
    print(find_factor(16))
    print(factorize(720))
