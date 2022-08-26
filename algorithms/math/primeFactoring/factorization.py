#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: August 25th, 2022

Algorithms for factoring numbers using Pollard's rho algorithm.
Runtime for finding a factor is about O(x**0.5), where x is the
smallest factor remaining. Realistically the algorithm should be
usable until 10^12.

Note: various print statements are stil being kept for debugging purposes,
these will be removed once the algorithm is fully functional.

factorize returns factors in 2d array, each array is [factor, freq]
"""
from math import gcd,sqrt,ceil,inf

def fact_func(x: int, r: int) -> int: #may need to use other c's than 1
    return (x*x+1) % r


def find_factor(n: int) -> int:
    x,y,a = 2,2,1

    while a != 1: #unsure how many iterations are needed here
        #i += 1
        x = fact_func(x,n)
        y = fact_func(fact_func(y,n),n)
        a = gcd(n,abs(x-y))
        if x == y:
            break

    return a

def div(n: int, ar: list, limit = inf) -> list[int]:

    if n == 1: return ar
    if n % 2 == 0:
        ar.append(2)
        return div(n//2,ar,limit)

    for i in range(3,min(limit,ceil(sqrt(n+1))),2): #3,5,7,...,sqrt(n)
        if n % i == 0:
            ar.append(i)
            return div(n//i,ar,limit)
    #n is prime
    ar.append(n)
    return ar

def trial_div(n: int, limit = inf) -> list[int]:
    if n == 2 or n == 3: return [n]
    else: return div(n,list(),limit)

def factorize(n: int) -> list[list[int]]:
    #break n into smaller factors
    d = {}
    while n != 1:
        x = find_factor(n)
        if d.get(x) == None: d[x] = 0
        d[x] += 1
        n = n // x
    k = list(d.keys())
    #print(d)
    #check each factor using trial div, not all may be prime
    #replacable with sieve
    for i in range(len(k)):
        #ar.append([k[i],d[k[i]]])
        a,b = k[i],d[k[i]]
        c = trial_div(a)
        if len(c) != 1:
            #print(a,c)
            for m in range(len(c)):
                if d.get(c[m]) == None: d[c[m]] = 0
                d[c[m]] += b
            d[a] = 0
    #translate from dict to list[int]
    k = list(d.keys())
    ans = list()
    for j in range(len(k)):
        if d[k[j]] != 0:
            ans.append([k[j],d[k[j]]])
    return ans




if __name__ == "__main__":
    #wip testing, formal testcases are wip
    #print(find_factor(1497631652873))
    #print(find_factor(16))
    print(factorize(720))
    #print(factorize(1497631652873*1497631652873))
    print(factorize((2*3*5*7*11*13*17*19*23*29)**100))
    print(trial_div(2*3*7*7*121*19*8))
