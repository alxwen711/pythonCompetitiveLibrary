"""
Author: alxwen711 (Alex Wen)
Last updated: August 4th, 2022

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

Note: This data structure will slow down significantly with a large
number of entries. It can handle up to about 500000 values added to
it in under a second consistently, but this will vary depending on
the testing system used. Further improvements that reduce the slowdown
from excessive memory usage are being looked at.
"""

class queue:
    def __init__(self):
        self.q = list()
        self.pt = 0
        self.l = 0

    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self):
        return self.l - self.pt

    def empty(self) -> bool:
        if self.pt == self.l: return True
        return False



if __name__ == "__main__":
    x = queue() #create new queue
    x.add(1)
    x.add(2)
    x.add(3)
    #queue is now [1,2,3]
    print(x.dequeue()) #should be 1
    print(x.top()) #should be 2
