"""
Author: alxwen711 (Alex Wen)
Last updated: November 4th, 2022

Ternary searching implementation, below the code has
been fitted for example usage as follows:

Given a "mountain" array (given n elements, for some
index i, A[:i] is strictly non-decreasing and A[i:]
is strictly non-increasing), find the largest value.
Ternary search can be used to find the largest value.
Choose two indicies a,b where 0 < a < b < n. If A[a] > A[b]
the max val has to be in A[:b]. if A[a] < A[b] the max val
has to be in A[a:]. If A[a] = A[b] max val is in A[a:b]. By
choosing a and b such that the remaining search range is split
into thirds, the program will effectively run in O(log n) time.


tfunc(x,ar)
Ternary function that will return 0, 1, or 2 depending on the input.
In practical use this should be adjusted as necessary for the problem.

tsearch(low,high,ar)
Ternary searching framework with low, high as the starting range limits.
ar is an optional value to use depending on the problem being solved.
The searching method is currently set to search the bottom 2/3rds of the
range if tfunc = 0, the top 2/3rds of the range if tfunc = 1, and the middle
1/3 if tfunc = 2. If the range is small enough (in this case, 3 or fewer values
to search), then the algorithm will brute force the solution on the remaining
values. Like tfunc, tsearch will be adjusted as needed based on the problem.


IMPORTANT NOTES:
The last line in tsearch is meant to brute force the answer over a small range
of remaining possible values and is dependent on problem being solved.

If the range being searched is not solely integers, replace tsearch's first three
lines with the following:
while high - low > x: (x = maximum error allowed)
    left = (high-low)/3+low
    right = (2*(high-low))/3+low
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
        if x == 0: low = left #left case
        elif x == 1: high = right #right case
        else: #center case
            low = left
            high = right

    #3 or fewer values in range, code edge case here
    return max(ar[low],ar[high],ar[(low+high)//2])


if __name__ == "__main__":
    #example use, guessing val from 1 to 1000000
    mountain_ar = [0,2,7,8,9,11,7,6,5,3,1]
    print(tsearch(0,len(mountain_ar)-1,mountain_ar))


