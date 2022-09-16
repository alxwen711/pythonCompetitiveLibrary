"""
Author: alxwen711 (Alex Wen)
Last updated: September 7th, 2022

Note: The mess of code in this file is being cleaned up with proper
documentation, but it is in a functional state for competitive programming.

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

factorize returns factors in 2d array, each array is [factor, freq]

prime(n)
Determines if n is prime. Returns answer as a boolean value.

trial(n,s,a,d)
Used as part of prime. If this function returns True, then
a "witness" was found in the prime test meaning that n is
not prime.

fact_func(x,r,c)
Helper function used for find_factor(n). Defines a generating function to find a
potential factor.

find_factor(n)
Helper function for factorize(n) used to find a factor of n. The factor returned
is usually prime, but in the case it isn't, factorize(n) can be tried to factor
it further, or trial_div if no progress is made. 

factorize(n)
Main method used for factoring. Given an integer n, returns a list of 2-tuples in
form [x,y], x is the prime factor and y is the frequency it is in n.

div(n)
actual function that does the work for trial_div()

trial_div(n)
Trial divison, used as a last resort for factorization. Hopefully any values that
end up here aren't too big. This part of the function only covers edge cases,
actual work is done by div.

"""
from math import gcd,sqrt,ceil
from random import randint


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


def trial(n: int, s: int, a: int, d: int) -> bool:
    val = pow(a,d,n)
    if val == 1 or val == n-1: return False
    for i in range(s-1):
        val = pow(val,2,n)
        if val == n-1: return False
    return True



#copy only the code above if you just need a primality test

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
     

#keep div and trial_div for completeness
def div(n: int, ar: list) -> list[int]:
    if n == 1: return ar
    if n % 2 == 0:
        ar.append(2)
        return div(n//2,ar)

    for i in range(3,ceil(sqrt(n+1)),2): #3,5,7,...,sqrt(n)
        if n % i == 0:
            ar.append(i)
            return div(n//i,ar)
    #n is prime
    ar.append(n)
    return ar


def trial_div(n: int) -> list[int]:
    if n <= 3: return [n]
    else: return div(n,list())




if __name__ == "__main__":
    print(factorize(720))
    print(factorize((2*3*5*7*11*13*17*19*23*29)**100)) #982 decimal digits
    print(trial_div(2*3*7*7*121*19*8))
