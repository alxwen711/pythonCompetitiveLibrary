#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: August 15th, 2022

Sparse table for returning range minimum queries (RMQ) in O(1) time.

"""



def sparse(ar):
    ans = list()
    ans.append(ar.copy())
    l = 1
    dist = 2
    while dist <= len(ar):
        tmp = list()
        for i in range(len(ar)-dist+1):
            #find [i:i+2**l]
            tmp.append(min(ans[l-1][i],ans[l-1][i+dist//2]))
        ans.append(tmp)
        l += 1
        dist *= 2
    return ans


def f(l,h,ar):
    length = h-l+1
    two = 1
    ex = 0
    while 2*two <= length:
        two = two*2
        ex += 1
    if length == two: return ar[ex][l]
    else: return min(ar[ex][l],ar[ex][h-two+1])


if __name__ == "__main__":
    x = [7,8,7,0,9,8,6,4,3]
    a = sparse(x)
    print(a)
    for i in range(len(x)):
        for j in range(i,len(x)):
            print(i,j,f(i,j,a))
            assert f(i,j,a) == min(x[i:j+1])
