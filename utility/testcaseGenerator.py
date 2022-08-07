#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: August 5th, 2022

Various useful functions for generating testcases.

note: docs will be updated after I feel enough actual generating functions are placed here
"""
from random import randint

def rand_array(n: int, low = 0, high = 100000000) -> list[int]:
    ar = list()
    for i in range(n):
        ar.append(randint(low,high))
    return ar

def print_array(n: int, ar) -> None:
    #use this to be able to generate typical testcase setups
    for i in range(n):
        print(*ar)

if __name__ == "__main__":
    print(rand_array(10,1,10)) #10 random values from 1 to 10
