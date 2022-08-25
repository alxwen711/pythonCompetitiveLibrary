#WIP
"""
Author: alxwen711 (Alex Wen)
Last update: August 25th, 2022

Statistics functions
"""




def avg(ar: list):
    return sum(ar)/len(ar)


def median(ar: list):
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
    return 1


def std_dev(ar: list):
    """
    let x = mean
    for each element i:
    let y = (i-x)^2
    sum each y found, divide by num of elements
    sqrt for std dev
    """





if __name__ == "__main__":
    #examples
