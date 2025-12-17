import pytest
import os,sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.data_structures.Stack import stack
from random import randint

def test_base(): 
    x = stack() #create new stack
    x.push(1)
    x.push(2)
    x.push(3)
    #stack is now [1,2,3]
    assert x.pop() == 3 #should be 3
    assert x.top() == 2 #should be 2
    assert x.length() == 2

def test_speed(): 
    n = 100000
    x = stack()
    ar = list()
    for i in range(n):
        y = randint(1,100000000)
        x.push(y)
        ar.append(y)
        assert x.length() == i+1
    for j in range(n):
        assert x.pop() == ar[-j-1]

def test_empty():
    x = stack()
    assert x.pop() == None # no error should be thrown

