#WIP, usable but documentation still needed
"""
n choose k mod r

describe each function in documentation here
fermat_array -> create array for solving up to given n choose k
fermat_comb -> for using fermat array

"""
def fermat_array(n: int, k: int, r: int) -> list[list[int],list[int]]:
    #factorials[n]*inverses[k]*inverses[n-k] % r for usage
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
    if k > n or n < 0 or k < 0 or r < 0 or facts == None or invs == None: return -1 
    return facts[n]*invs[k]*invs[n-k] % r


if __name__ == "__main__":
    #include tests here
    r = 100000007
    facts,invs = fermat_array(100,100,r)
    n = 10
    k = 0
    print(str(n),"choose",str(k),"is",str(fermat_comb(n,k,r,facts,invs)))
    
