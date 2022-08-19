"""
Author: alxwen711 (Alex Wen)
Last updated: August 5th, 2022

Various useful functions for generating testcases
and running testcode.

rand_array(n,[low,high])
Generates an list[int] of n elements from low to high
default range is 1 to 1000000000

print_array(ar,[n])
Prints each element in an array separated by spaces n times
default n value is 1
"""
from random import randint

def rand_array(n: int, low = 1, high = 100000000) -> list[int]:
    ar = list()
    for i in range(n):
        ar.append(randint(low,high))
    return ar

def print_array(ar: list,n = 1) -> None:
    #use this to be able to generate typical testcase setups
    for i in range(n):
        print(*ar)

if __name__ == "__main__":
    n = 5 #number of testcases
    print(n)
    for i in range(n):
        a,b = 10,randint(1,10) #first line variables
        print(a,b)
        print_array(rand_array(a,1,100)) #10 random values from 1 to 10
