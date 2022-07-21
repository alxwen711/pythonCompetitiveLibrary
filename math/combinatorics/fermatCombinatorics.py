"""
Author: alxwen711 (Alex Wen)
Last updated: 7/20/22

Fermat algorithms for quickly calculating n choose k mod r
Note: fermat_array does not work if r < 2, in this case use
the single case function fermat_calc.

fermat_array(n,k,r)
returns two arrays facts and invs to be used with fermat_comb
parameters inserted are the maximum values, ie. for calculating
100 choose 50 mod 727 using this function, parameters should be
fermat_array(100,50,727)


fermat_comb(n,k,r,facts,invs)
returns n choose k mod r
must use fermat_array to get facts and invs

"""
def fermat_array(n: int, k: int, r: int) -> list[list[int],list[int]]:
    #O(n log n) time
    if k >= r or r < 3: return None, None 
    arLen = n+k+3 #array length
    factorials = [0]*arLen
    inverses = [0]*arLen
    factorials[0], inverses[0] = 1,1
    for i in range(1,arLen):
        factorials[i] = factorials[i-1]*i % r
        inverses[i] = pow(factorials[i],r-2,r)
    return factorials, inverses


def fermat_comb(n: int, k: int, r: int, facts: list[int], invs: list[int]) -> int:
    #O(1) lookup time
    if facts == None or invs == None or r == 0: return -1 #array or div 0 error
    #trivial cases
    if k > n or r == 1: return 0 
    if n == 0 or k == 0: return 1
    return facts[n]*invs[k]*invs[n-k] % r


if __name__ == "__main__":
    #include example use here
    r = 100000007
    facts,invs = fermat_array(100,100,r)
    n = 10
    k = 0
    print(str(n),"choose",str(k),"is",str(fermat_comb(n,k,r,facts,invs)))
    
