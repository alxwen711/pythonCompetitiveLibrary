"""
Author: alxwen711 (Alex Wen)
Last updated: August 7th, 2022

Algorithms for finding the area of a convex polygon.

- triangles + Heron's formula
- Shoelace method (to be updated)

note: value is only consistently accurate to ~13-14 significant figures.

points input are expected to be in the format
[[x1,y1],[x2,y2],[x3,y3],[x4,y4]...]
"""

from math import sqrt

def pythagoras(pt_a: list, pt_b: list) -> float:
    return sqrt((pt_a[0]-pt_b[0])**2+(pt_a[1]-pt_b[1])**2)

def heron_triangle(a: float, b: float, c: float) -> float:
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

def heron_area(ar: list[list]) -> float:
    ans = 0
    for i in range(len(ar)-2):
        x,y = i+1,i+2
        a = pythagoras(ar[0],ar[x])
        b = pythagoras(ar[0],ar[y])
        c = pythagoras(ar[x],ar[y])
        ans += heron_triangle(a,b,c)
    return ans
    

if __name__ == "__main__":
    #example use
    print(heron_area([[0,0],[0,20000],[20000,20000],[20000,0]]))
