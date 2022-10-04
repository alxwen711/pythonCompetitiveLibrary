"""
Author: alxwen711 (Alex Wen)
Last updated: October 4th, 2022

Ternary searching implementation, docs to be updated soon


tfunc(x,ar)
Boolean function to determine if the low or high endpoint of the binary
search range needs to be adjusted. ar is an optional value that can be
passed depending on the problem.

tsearch(low,high,ar)
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

def tfunc(left, right, ar = None):
    #for example use
    x,y = ar[left],ar[right]
    if x < y: return 0
    elif x > y: return 1
    else: return 2


def tsearch(low, high, ar = None):
    while high - low > 2:
        left = (high-low)//3+low
        right = (2*(high-low))//3+low
        x = tfunc(left,right,ar)
        if x == 0: low = left
        elif x == 1: high = right
        else:
            low = left
            high = right
            
    #3 or fewer values in range, code edge case here
    return max(ar[low],ar[high],ar[(low+high)//2])
if __name__ == "__main__":
    #example use, guessing val from 1 to 1000000
    mountain_ar = [0,2,7,8,9,11,7,6,5,3,1]
    print(tsearch(0,len(mountain_ar)-1,mountain_ar))


