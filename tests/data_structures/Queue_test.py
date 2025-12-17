import pytest
import os,sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.data_structures.Queue import queue

from random import randint

def test_basic():
    x = queue() #create new queue
    x.add(1)
    x.add(2)
    x.add(3)
    #queue is now [1,2,3]
    assert x.dequeue() == 1 #should be 1
    assert x.top() == 2 #should be 2
    x.add(5)
    x.add(4)
    #queue is now [2,3,5,4]
    assert x.dequeue() == 2 #should be 2
    assert x.dequeue() == 3 #should be 3

def test_speed(): #efficiency test, should be done in 1 second tops
    x = queue()
    num = 500000
    for i in range(num):
        x.add(randint(1,1000000000))
    for _ in range(num):
        assert x.dequeue() != None
    assert x.dequeue() == None 
    
        
