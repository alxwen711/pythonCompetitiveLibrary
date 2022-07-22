#WIP template for seg tree (still needs docs, how to edit)
"""
var notes for documentation/refactoring:
lr -> left range
rr -> right range
lc -> left child
rc -> right child
n -> node
nl -> len(nodes)

current setup is for returning maximum of any given contiguous subarray
O(n) set up time, O(log n) queries
"""

import sys

class Tree:
    def __init__(self,val,lr,rr,lc,rc):
        self.val = val
        self.lr = lr
        self.rr = rr
        self.lc = lc
        self.rc = rc
        
def look(l,r,n): #searching function
    if l == n.lr and r == n.rr: return n.val
    if n.lc == None: return look(l,r,n.rc)
    #dual node setup
    a,b,c,d = n.lc.lr,n.lc.rr,n.rc.lr,n.rc.rr
    x,y = 0,0
    if l <= b: #left is involved
        if l == a and r >= b: #all left
            x = n.lc.val
        else: x = look(l,min(b,r),n.lc)
    if r >= c: #right is involved
        if r == d and l <= c: #all right
            y = n.rc.val
        else: y = look(max(c,l),r,n.rc)
    return max(x,y)



def create_segtree(ar: list[int]) -> Tree:
    m = len(ar)
    nodes = list()
    for i in range(m):
        tmp = Tree(ar[i],i,i,None,None)
        nodes.append(tmp)
    nl = m
    while nl != 1:
        #print(nl,len(nodes))
        nn = list()
        for j in range(nl//2):
            left,right = nodes[2*j],nodes[2*j+1]
            tmp = Tree(max(left.val,right.val),left.lr,right.rr,left,right)
            nn.append(tmp)
        if nl % 2 == 1:
            right = nodes[-1]
            tmp = Tree(right.val,right.lr,right.rr,None,right)
            nn.append(tmp)
            nl += 1
        nl = nl // 2
        nodes = nn
    return nodes[0]

if __name__ == "__main__":
    #example use
    ar = [8,2,9,3,7,4,3,5]
    segtree = create_segtree(ar)
    print("maximum from index 3 to index 6 is:",str(look(3,6,segtree)))
    print("expected value is:",str(max(ar[3:7])))
    


