"""
Author: alxwen711 (Alex Wen)
Last updated: August 6th, 2022

Set of functions for returning the frequency of each value in
an integer array in either another array or a dictionary. For
character based arrays use strhashmaps.

All functions take O(n) time to complete.

freq_ar(ar,limit)
Returns a frequency array h where h[x-1] contains the number of
times value x shows up in ar. limit is supposed to be the maximum
value in ar and controls the size of h. If ar is None then an empty
array is returned.

Warning: freq_ar will exceed memory limits of most contests if limit
is too high. On Codeforces this will happen if limit = 10^9.

freq_dict(ar,pos)
Returns a dictionary d where d[x] contains either:
- the number of times x shows up in ar if pos == False (default value)
- an array containing the indices where x is located in ar if pos == True
If ar is None then an empty dict is returned.
"""

from random import randint #for example use

def freq_ar(ar: list[int], limit: int) -> list[int]:
    if ar == None: return []
    h = [0]*limit #change to limit+1 for h[1] = freq of 1
    for i in range(len(ar)):
        h[ar[i]-1] += 1 #change to h[ar[i]] for h[1] = freq of 1
    return h

def freq_dict(ar: list[int], pos = False) -> dict:
    d = {}
    if ar == None: return d
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
    print("frequency dictionary:",str(freq_dict(ar)))
    print("dict with position:",str(freq_dict(ar,True)))
        
