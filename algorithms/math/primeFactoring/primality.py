#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: August 26th, 2022

Miller-Rabin primality test implementation. This is a probabilistic test,
meaning that correct prime/composite determination is not guarenteed.
That said the test uses 100 trials, and the chance of a false positive is
at most 1 in 4^100 (about 1.6*10^60). Runtime is supposed to be O(k*(log n)^3),
where k is the number of trials and n is the value being tested.
Further testing to confirm this is needed.

Steps:
Check if n is even (if yes, 2 is prime, else comp)
Check if n is 3, if so prime (edge case)
n-1 = 2^s*d, d is odd, solve for s and d
Choose a value from 2 to n-2 inclusive, let this be a
For 0 to s-1 inclusive (let this be r), check if any of these satifies the following:
a^((2^r)*d) % n == n-1 (or 1 if r == 0)
if r does not exist, n is comp
else try again with new a value
repeat until enough a values are tested, n is (most likely) prime
"""
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

if __name__ == "__main__":
    for j in range(5):
        x = randint(1,100)
        if prime(x): print(x,"is prime")
        else: print(x,"is not prime")
