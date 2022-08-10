"""
Author: alxwen711 (Alex Wen)
Last updated: August 10th, 2022

Template for the stack data structure. The stack is made up of a 1D
mutuable array. All stack methods are optimized to run as fast as
possible (O(1) per operation).

push(x)
adds element x to the stack.

pop()
returns and removes the top element in the stack.

top()
returns the top element in the stack, but does not remove it.

len()
returns the number of elements in the stack.
"""

class stack:
    def __init__(self):
        self.s = list()

    def push(self,x) -> None:
        self.s.append(x)

    def pop(self):
        if self.length() == 0: return None #empty list
        x = self.s.pop()
        return x

    def top(self):
        return self.s[-1]

    def length(self) -> int:
        return len(self.s)

if __name__ == "__main__":
    x = stack() #create new stack
    x.push(1)
    x.push(2)
    x.push(3)
    #stack is now [1,2,3]
    print(x.pop()) #should be 3
    print(x.top()) #should be 2
