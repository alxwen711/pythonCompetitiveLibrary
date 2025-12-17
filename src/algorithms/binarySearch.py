"""
Author: alxwen711 (Alex Wen)
Last updated: July 28th, 2022

Basic algorithm build for problems where the solution is reliant
on binary searching. A bsearch query will take O(log n * x) time,
where x = runtime of bfunc. The example setup below involves the
function guessing a random number from 1 to 1000000 being told if
the number is too low or not.

bfunc(x,ar)
Boolean function to determine if the low or high endpoint of the binary
search range needs to be adjusted. ar is an optional value that can be
passed depending on the problem.

bsearch(low,high,ar)
Binary searching framework. low and high are the range endpoints to
binary search on. ar is an optional value that can be passed depending
on the problem.

IMPORTANT NOTES:
The functions are default set to adjust the high endpoint if bfunc returns
True and to adjust the low endpoint if bfunc returns False.

The second last line in bsearch may need to be adjusted to test the low endpoint
depending on the problem.

If the range being searched is not solely integers, replace bsearch's first two
lines with the following:
while high - low > x: (x = maximum error allowed)
    mid = (low+high)/2
"""

def bfunc(x, ar = None) -> bool:
    #for example use
    if x >= ar: return True
    return False


def bsearch(low, high, ar = None):
    while high - low > 1:
        mid = (low+high)//2 
        if bfunc(mid,ar): high = mid
        else: low = mid

    #diff is small enough
    if bfunc(high,ar): return high
    else: return low

if __name__ == "__main__":
    #example use, guessing val from 1 to 1000000
    from random import randint
    val = randint(1,1000000)
    print("value to guess:",val)
    print("value from bsearch:",bsearch(1,1000000,val))




