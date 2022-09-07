#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: September 7th, 2022

Various algorithms for determining if a number is prime and factorization.
This file is a merging of former primality.py and factorization.py.

Possible framework for factorization:

1. check if prime first
2. if not prime, run factor find up to 10 times to find a factor
3. once factor is found, add to dict
4. repeat 1 to 3 until prime
5. check each factor, if not prime run 2.
6. Convert to array

Algorithms for factoring numbers using Pollard's rho algorithm.
Runtime for finding a factor is about O(x**0.5), where x is the
smallest factor remaining. Realistically the algorithm should be
usable until 10^10.

Note: various print statements are stil being kept for debugging purposes,
these will be removed once the algorithm is fully functional.

factorize returns factors in 2d array, each array is [factor, freq]
"""
from math import gcd,sqrt,ceil,inf
from random import randint

def trial(n: int, s: int, a: int, d: int) -> bool:
    val = pow(a,d,n)
    if val == 1 or val == n-1: return False
    for i in range(s-1):
        val = pow(val,2,n)
        if val == n-1: return False
    return True

def prime(n: int) -> bool:
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n <= 1: return False
    d,s = n-1,0
    while d % 2 == 0:
        s += 1
        d = d // 2
    for i in range(100):
        a = randint(2,n-2)
        if trial(n,s,a,d): return False
    return True



def fact_func(x: int, r: int, c: int) -> int: #may need to use other c's than 1
    return (x*x+c) % r


def find_factor(n: int) -> int: #assume a composite number is given
    for c in range(1,11):
        if c >= n: break
        x,y,a = 2,2,1
        while a == 1: #unsure how many iterations are needed here
            x = fact_func(x,n,c)
            y = fact_func(fact_func(y,n,c),n,c)
            a = gcd(n,abs(x-y))
            if x == y:
                break
        if a != n: break #factor has been found
    return a


def factorize(n: int) -> list[list[int]]:
    if n <= 3: return [[n,1]] #0-1 edge cases
    #break n into smaller factors
    d = {}
    while not prime(n) and n != 1:
        x = find_factor(n)
        if d.get(x) == None: d[x] = 0
        d[x] += 1
        n = n // x
    if n != 1:
        if d.get(n) == None: d[n] = 0
        d[n] += 1
    
    #check factors
    k = list(d.keys())
    for i in range(len(k)):
        a,b = k[i],d[k[i]]
        if not prime(a):
            c = trial_div(a)
            for j in range(len(c)):
                factor = c[j]
                if d.get(factor) == None: d[factor] = 0
                d[factor] += b
            """
            wip method using factorize recursively
            c = factorize(a)
            for j in range(len(c)):
                factor,freq = c[j][0], c[j][1]
                if d.get(factor) == None: d[factor] = 0
                d[factor] += (freq*b)
            """
            d[a] = 0
            
    #translate from dict to list[int]
    k = list(d.keys())
    ans = list()
    for j in range(len(k)):
        if d[k[j]] != 0:
            ans.append([k[j],d[k[j]]])
    return ans
        
    """
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
"""

#keep div and trial_div for completeness
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
    if n <= 3: return [n]
    else: return div(n,list(),limit)




if __name__ == "__main__":
    #wip testing, formal testcases are wip
    #print(find_factor(1497631652873))
    #print(find_factor(16))
    print(factorize(720))
    #print(factorize(1497631652873*1497631652873))
    print(factorize((2*3*5*7*11*13*17*19*23*29)**100)) #982 decimal digits
    print(trial_div(2*3*7*7*121*19*8))
