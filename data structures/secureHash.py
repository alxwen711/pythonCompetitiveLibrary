#WIP
"""
Author: alxwen711 (Alex Wen)
Last updated: September 8th, 2022


This is designed to be a dictionary/hashmap structure
that is much harder to exploit. For now I'll call it
the Randomized Anti Codeforces Hashmap (RACH).

Currently supports integer keys only. Float keys may be
added if I find python's normal dict to be exploitable
there as well.

Good luck hacking this. Only drawback is that using
this is slightly inconvinient, but it's easily better
than losing 100 ELO due to being hacked. Yes I may
still be salty over one specific incident.
"""

from secrets import randbelow
from random import shuffle
_MAX = 2**64-1
class hashmap:
    def __init__(self):
        self.f,self.q,self.l = randbelow(420),list(),list()
        self.d,self.c = list(),randbelow(_MAX)
        for potato in range(100):
            self.d.append(randbelow(_MAX))
            self.l.append({})
            self.q.append(potato)
        shuffle(self.q)
        
    def decode(self, x: int) -> list[dict,int]:
        x = x ^ self.c
        xx = (x+self.f) % 100
        hm = self.l[self.q[xx]]
        x = x ^ self.d[xx]
        return hm,x


if __name__ == "__main__":
    print("lol you ain't breaking this")
    d = hashmap()
    print(d.decode(100))
