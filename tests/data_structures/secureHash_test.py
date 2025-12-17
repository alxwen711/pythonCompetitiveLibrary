import pytest
import os,sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.data_structures.secureHash import * 

#create breaker here
ar = list()
ar.append(2**17+1)
ar.append(2**17+1)
mask = 2**17 - 1
x = 6
for i in range(99999):
    ar.append(x)
    ar.append(x)
    x = (x * 5 + 1) & mask

# print(ar[:10])

def test_million_overkill(): #speed test with 1000000 elements
    d = hashmap()
    n = 1000000
    for i in range(n):
        assert d.inc(i,1) == 1 #no individual value should map to same key and dict

def test_adverse_overkill(): #100000 num sequence meant to cause collisions
    d = hashmap()
    for i in range(200000):
        assert d.inc(ar[i],1) <= 2

     