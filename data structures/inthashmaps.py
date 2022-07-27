#WIP, add proper documentation
"""
Author: alxwen711 (Alex Wen)
Last updated: July 27th, 2022

frequency map/hash table file

given array, return frequency of each value in array/dict
with dict exact positions can be located
letter variations can be included here as well

func_a(x,y,z)
[explain func_a and its parameters]
func_b(x,y)
[explain func_b and its parameters]
Other useful things to note for documenting:
- Edge cases that the algorithm may not work for
- Runtime (O(1),O(log n),O(n),O(n^2),etc.)
"""

from random import randint #for example use

def freq_ar(ar: list[int], limit: int) -> list[int]:
    h = [0]*limit #change to limit+1 if you want h[1] = freq of 1
    for i in range(len(ar)):
        h[ar[i]-1] += 1 #change to h[ar[i]] if you want h[1] = freq of 1
    return h

def freq_dict(ar: list[int], pos: bool) -> dict:
    d = {}
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None:
            if pos: d[x] = list()
            else: d[x] = 0
        if pos: d[x].append(i)
        else: d[x] += 1
    return d


if __name__ == "__main__":
    #example use
    ar = list()
    for i in range(10):
        ar.append(randint(1,5))
    print("given array:",str(ar))
    print("freqency array:",str(freq_ar(ar,5)))
    print("frequency dictionary:",str(freq_dict(ar,False)))
    print("dict with position:",str(freq_dict(ar,True)))
        
