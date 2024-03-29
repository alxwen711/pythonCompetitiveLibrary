"""
Author: alxwen711 (Alex Wen)

Last updated: November 9th, 2022

O(n) implementation of the Knuth-Morris-Pratt algorithm for finding the longest
prefix for each element in a string or array.

prefix(x)
Given a string/array x, returns a prefix array containing the prefix values
for each element.

As an example, "abaaaba" returns [0,0,1,1,1,2,3]; last value
is a 3 since the last 3 characters equal the first 3 characters.
other values in the array only consider the first i+1 characters.
"""

def prefix(x):
    ar = [0]*len(x)
    for i in range(1,len(x)):
        v = ar[i-1]
        while x[i] != x[v] and v > 0: #stop when possible match is found
            v = ar[v-1]
        if x[i] == x[v]: #if false, no prefix found -> 0
            v += 1
        ar[i] = v
    return ar


if __name__ == "__main__":
    string = "abaaaba"
    print("prefix array for "+string+":")
    print(prefix(string))
