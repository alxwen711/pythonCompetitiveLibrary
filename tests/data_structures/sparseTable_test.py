import os,sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.data_structures.sparseTable import * 
from random import randint


def test_normal(): #test every range possible in small array
    x = [7,8,7,0,9,8,6,4,3,1,9,2,0,0,89,2]
    a = create_sparse(x) #create table
    assert a != None
    for i in range(len(x)):
        for j in range(i,len(x)):
            assert query(i,j,a) == min(x[i:j+1])

def test_speed():
    #table creation time is O(n log n), should take just under 1 second
    n = 100000
    ar = [0]*n
    for i in range(n):
        ar[i] = i
    t = create_sparse(ar) #create table
    for j in range(n): #100000 random ranges, each with O(1) runtime
        a,b = randint(0,n-1),randint(0,n-1)
        assert query(min(a,b),max(a,b),t) == min(a,b)

def test_single(): #test single value ranges
    n = 1000
    ar = [0]*n
    for i in range(n):
        ar[i] = randint(0,1000000000)
    t = create_sparse(ar) #create table
    for j in range(n):
        assert query(j,j,t) == ar[j]

