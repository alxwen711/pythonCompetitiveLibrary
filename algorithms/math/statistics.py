#WIP
"""
Author: alxwen711 (Alex Wen)
Last update: August 25th, 2022

Statistics functions

avg(ar)

median(ar)

mode(ar)

std_dev(ar)

"""


def avg(ar: list):
    if len(ar) == 0: return None
    return sum(ar)/len(ar)


def median(ar: list):
    if len(ar) == 0: return None
    br = ar.copy()
    br.sort()
    x = len(ar)
    if x % 2 == 1: return br[x//2]
    else:
        try: #return avg of two mid vals
            return (br[x//2-1]+br[x//2])/2
        except: #return left val
            return br[x//2-1]

def mode(ar: list):
    """
    use freq_dict in some way here? return as list for mult modes
    """
    if len(ar) == 0: return None
    d = {}
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None: d[x] = 0
        d[x] += 1
    #use keys here
    return 1


def std_dev(ar: list):
    """
    let x = mean
    for each element i:
    let y = (i-x)^2
    sum each y found, divide by num of elements
    sqrt for std dev
    """
    mean,n = avg(ar),len(ar)
    diff = 0
    for i in range(n):
        diff += (mean-ar[i])**2
    return (diff / n) ** 0.5




from random import randint
if __name__ == "__main__":
    ar = list()
    for i in range(10):
        ar.append(randint(0,10))
    print("array:",ar)
    print("mean:",avg(ar))
    print("median:",median(ar))
    print("mode:",mode(ar))
    print("stddev:",std_dev(ar))
    
