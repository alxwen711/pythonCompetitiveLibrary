"""
Author: alxwen711 (Alex Wen)
Last updated: October 13th, 2022

Template for the queue data structure. The stack is made up of a 1D
mutuable array. All queue methods are optimized to run as fast as
possible. length tracks the number of elements added to the queue and
pt tracks how many elements have been dequeued.

add(x)
adds element x to the queue.

dequeue()
returns and removes the top element in the queue. Note that a setup
using self.q.pop(0) would take O(n) time per query.

top()
returns the next element in the queue, but does not remove it.

length()
returns the number of elements in the queue.

empty()
checks if the queue is empty.

Oct 13th update: a memory refresh mechanism has been added so that once 
100000 elements in are dequeued, the first 100000 values in the queue
array are discarded to slightly reduce memory slowdown.
"""

class queue:
    def __init__(self,limit=100000):
        self.q = list()
        self.pt = 0
        self.l = 0
        self.memRefresh = limit

    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        #check if memory needs to be refreshed
        if self.pt == self.memRefresh:
            self.pt = 0
            self.l -= self.memRefresh
            self.q = self.q[self.memRefresh:]
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self) -> int:
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l



if __name__ == "__main__":
    x = queue() #create new queue
    x.add(1)
    x.add(2)
    x.add(3)
    #queue is now [1,2,3]
    print(x.dequeue()) #should be 1
    print(x.top()) #should be 2
