"""
Author: alxwen711 (Alex Wen)
Last updated: September 13th, 2022

Diophantine equation solver, ie. equations in the form ax + by = c
Algorithm is modelled off of https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Example

dio(a,b,c)

For the equation ax+by = c, a solution in the form (x,y) is returned as
4 values (s,t,u,v), where all possible solutions are in the form (s+nu,t-nv)
n is an integer.

returns two values containing the integer solution to ax+by = c
first value returned is a possible x value that gives an integer solution
second value returned is the positive increment for x.

If (-1,-1,-1,-1) is returned, then there is no solution.

Example: suppose the returned values are (5,3,7,2)
The set of (x,y) solutions can be written as (5+7n,3-2n), n is an integer
possible solutions are (5,3), (12,1), (-2,5), etc.
"""

from math import gcd

def dio(a: int, b: int, c: int):
    #trivial a = b case
    if a == b: 
        if c % a != 0:
            #return -1,-1
            return -1,-1,-1,-1
        else:
            #return 0,1
            return 0,c//b,1,1
        
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
    if c % g[-1] != 0: return -1,-1,-1,-1

    #solution exists s[-1],t[-1]
    ansa,ansb = s[-1],t[-1]
    ansa *= c//g[-1]
    ansb *= c//g[-1]
    ac = b//g[-1]
    bc = a//g[-1]

    #return ansa,ac
    return ansa,ansb,ac,bc



if __name__ == "__main__":
    a,b,c = 3,5,2
    x,y,v,w = dio(a,b,c)
    print("possible solutions to "+str(a)+"x "+"+ "+str(b)+"y = "+str(c)+":")
    print("x =",x,", y =",y)
    print("x =",x+v,", y =",y-w)
