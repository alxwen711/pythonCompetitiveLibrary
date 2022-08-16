#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: August 15th, 2022

Sparse table for returning range minimum queries (RMQ) in O(1) time.
Initial creation of the table takes O(n log n) time.
The functions below can be altered for other sparse table uses.

create_sparse(ar)
Creates a sparse array given an array ar. This is usually used with
list[int] but can be easily modified for other list types.
Format will be A[x][y] where a 2**x length subarray is covered starting
from index y. Example: A[2][3] covers indices 3 to 6 inclusive.

query(l,r,ar)
Runs a query using a created sparse table. This query normally takes O(1) time,
but can be used similarly to a segment tree for O(log n) queries. Doing this
will require significant edits to this function.
"""



def create_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    l = 1
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        tmp = list()
        for i in range(len(ar)-dist+1):
            #find [i:i+dist]
            tmp.append(min(s[l-1][i],s[l-1][i+dist//2]))
        s.append(tmp)
        l += 1
        dist *= 2
    return s


def query(l: int, h: int, ar: list[list]):
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while 2*two <= length:
        two = two*2
        ex += 1
    if length == two: return ar[ex][l]
    else: return min(ar[ex][l],ar[ex][h-two+1])


if __name__ == "__main__":
    x = [7,8,7,0,9,8,6,4,3]
    a = create_sparse(x)
    #print(a), contains sparse table
    for i in range(len(x)):
        for j in range(i,len(x)):
            #print(i,j,query(i,j,a)) for validation
            assert query(i,j,a) == min(x[i:j+1])
