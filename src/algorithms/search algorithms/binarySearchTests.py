import unittest
from random import randint

#binarySearch.py is copied for the examples here to demonstrate bfunc modularity

"""
example use with a trivial problem
given a square number, determine its square root (no using **.5/sqrt)
note that log(100000000,base=2) is about 26.5, O(26.5n) may be a factor
in problems with a 1 second time limit
"""     

def bfunc(x: int, ar = None) -> bool:
    #this function is edited for use case
    if x**2 >= ar: return True
    return False

def bsearch(low: int, high: int, ar = None) -> int:
    while high - low > 1:
        mid = (low+high)//2
        if bfunc(mid,ar): high = mid
        else: low = mid

    #diff between high and low is 1 (or 0)
    if bfunc(high,ar): return high
    else: return low


class algorithm_test(unittest.TestCase):

    def test_square(self):
        for i in range(100000):
            v = randint(1,100000000) #value to guess
            self.assertEqual(bsearch(1,100000000,v**2),v)

"""
binarySearch example using Problem 1701C on Codeforces
https://codeforces.com/contest/1701/problem/C
solve method is a helper method for the problem
freq_ar is a helper method found in inthashmaps.py
"""

def bfunc2(x: int, ar: list[int], n: int, m: int) -> bool:
    tasks = 0
    for k in range(n):
        if ar[k] >= x: tasks += x
        else:
            tasks += ar[k]
            tasks += (x-ar[k])//2
        if tasks >= m: return True
    return False

def bsearch2(low: int, high: int, ar = None) -> int:
    n = len(ar)
    m = high//2
    while high - low > 1:
        mid = (low+high)//2
        if bfunc2(mid,ar,n,m): high = mid
        else: low = mid
    
    #diff between high and low is 1 (or 0)
    if bfunc2(low,ar,n,m): return low
    else: return high

def freq_ar(ar: list[int], limit: int) -> list[int]:
    if ar == None: return []
    h = [0]*limit #change to limit+1 for h[1] = freq of 1
    for i in range(len(ar)):
        h[ar[i]-1] += 1 #change to h[ar[i]] for h[1] = freq of 1
    return h

def solve(n: int, m: int, ar: list[int]) -> int:
    h = freq_ar(ar,n)
    return bsearch2(1,2*m,h)

class codeforces_test(unittest.TestCase):
    
    def test_case1(self):
        #identical to testcase 1
        self.assertEqual(solve(2,4,[1,2,1,2]),2)
        self.assertEqual(solve(2,4,[1,1,1,1]),3)
        self.assertEqual(solve(5,5,[5,1,3,2,4]),1)
        self.assertEqual(solve(1,1,[1]),1)
        

if __name__ == "__main__":
    unittest.main()
