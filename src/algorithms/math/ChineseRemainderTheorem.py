#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: September 14th, 2022

Implementation of the Chinese Remainder Theorem

Right now I'm still figuring out how to implement this, notes
are being kept here as pseudocode:

- modular inverse is value a such that ax % m = 1


- given n statements of x % m = a, and all m values are coprime:
- for each equation, find the following:
- S = product of all m
- Z = S/m, find for each equation
- z = modular inverse of Z%m (solve for x, xZ % m = 1)
- y = z mod m
- w = yz mod S
- c = sum of aw from each equation
- Solution is c + nS, n is an integer

Practice: 1665D, use CRT

using dio(a,m,1) gives inverse??
ax+my = 1 (Bezout’s identity is true if = gcd(a,m))
a mod m = 1
ax mod m = 1, x is the inverse

inverse(a,m)
return modular inverse of a % m

crt(list[list[int,int]])
given n pairs of (m,r) from a % m = r, return a solution
in the form c + nS, c is the lowest positive value and S
is the increment. ie. something like 8,21 would be interpreted
as the solution can be 8,29,60,81...

This algorithm assumes all m values are coprime.


simplify(list[list[int,int]])
makes sure all m values are coprime, else check that a solution can
even exist and remove the lower unneeded m values/ simplify them.
"""

from math import gcd

#from diophantine.py, to be adjusted for this algorithm
def dio(a: int, b: int, c: int) -> list[int,int]:
    #trivial a = b case
    if a == b: 
        if c % a != 0: return -1,-1
        else: return 0,1
        
    #use extended euclidian algorithm
    g = list() #gcd
    s = list() #a coeff
    t = list() #b coeff
    if a > b:
        g.append(a);g.append(b)
        s.append(1);t.append(0)
        s.append(0);t.append(1)
    else:
        g.append(b);g.append(a)
        s.append(0);t.append(1)
        s.append(1);t.append(0)
    while True:
        q = g[-2] // g[-1]
        r = g[-2]-(g[-1]*q)
        if r == 0: break
        g.append(r)
        s.append(s[-2]-(s[-1]*q))
        t.append(t[-2]-(t[-1]*q))
    if c % g[-1] != 0: return -1,-1

    #solution exists s[-1],t[-1]
    ansa,ansb = s[-1],t[-1]
    ansa *= c//g[-1]
    ansb *= c//g[-1]
    ac = b//g[-1]

    return ansa,ac











if __name__ == "__main__":
    #do stuff here
