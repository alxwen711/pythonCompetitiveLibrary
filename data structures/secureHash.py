#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: September 8th, 2022


This is designed to be a dictionary/hashmap structure
that is much harder to exploit. For now I'll call it
the Randomized Anti Codeforces Hashmap (RACH).

Note that I'm designing this to be as convoluted as possible,
so the normal guidelines of "clear and understandable" code
are not in effect here.

Good luck hacking this.
"""

from secrets import randbelow as r 
_z = 2**64-1
class hashmap:
    def __init__(self):
        self.f,self.q,self.l = r(_z),list(),list()
        self.d,self.c = list(),r(420)




if __name__ == "__main__":
    print("lol you ain't breaking this")

