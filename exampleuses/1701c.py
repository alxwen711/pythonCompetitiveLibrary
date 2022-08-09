import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


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

for i in range(readint()):
    n,m = readints()
    ar = readar()
    print(solve(n,m,ar))

