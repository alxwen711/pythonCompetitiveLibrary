"""
Author: alxwen711 (Alex Wen)
Last updated: October 5th, 2022

Sparse table for returning range minimum queries (RMQ) in O(1) time.
Initial creation of the table takes O(n log n) time.
The functions below can be altered for other sparse table uses.
The default settings are for returning the minimum value in a subarray.

create_sparse(ar)
Creates a sparse array given an array ar. This is usually used with
list[int] but can be easily modified for other list types.
Format will be A[x][y] where a 2**x length subarray is covered starting
from index y. Example: A[2][3] covers indices 3 to 6 inclusive.

query(l,r,ar)
Runs a query using a created sparse table. This query normally takes O(1) time,
but can be used similarly to a segment tree for O(log n) queries. Doing this
will require significant edits to this function.

exact_query(l,r,ar)
Similar to query, but will instead find exact subarray fragments to create the
subarray, ie. for query(3,12,A), subarrays A[3:11] and A[5:13] will be used,
but exact_query(3,12,A) will call A[3:11] and A[11:13]. This method takes O(log n)
time to run.
"""

def create_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (min(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def query(l: int, h: int, ar: list):
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l]
    else: return min(ar[ex][l],ar[ex][h-two+1])

def exact_query(l: int, h: int, ar: list):
    #default setting is to find minimum of subarray
    length = h-l+1
    s = str(bin(length))[2:]
    two = len(s)
    pt = l
    ans = 9999999999999999999999999 
    for i in range(two):
        if s[i] == "1":
            ans = min(ans,ar[two-i-1][pt])
            pt += 2**(two-i-1)
    return ans
            


if __name__ == "__main__":
    x = [7,8,7,0,9,8,6,4,3]
    a = create_sparse(x)
    #print(a), contains sparse table
    for i in range(len(x)):
        for j in range(i,len(x)):
            #print(i,j,query(i,j,a)) for validation
            assert query(i,j,a) == min(x[i:j+1])
            assert exact_query(i,j,a) == min(x[i:j+1])
            
