"""
Author: alxwen711 (Alex Wen)
Last updated: July 27th, 2022

Segment tree template; main use is for problems where queries involving
a contiguous subarray are numerous. Assuming that the segment function is
O(1) time, the segment tree takes O(n) time to create and completes
queries in O(log n) time.

class Tree
Defines node object for the segment tree. lr/rr determines the
subarray's endpoints, val(ue) is determined by seg_func(), and
lc/rc stands for left child/right child respectively.

seg_func(a,b)
function for defining the value stored in the seg tree. a and b are two
values obtained from two different nodes in the tree.

create_segtree(ar)
creates a segtree with the given ar(ray).

seg_search(left,right,node)
returns the value for subarray [left,right] inclusive.
node to be given is the head node of the Tree to be searched.
"""

class Tree:
    def __init__(self,val,lr,rr,lc,rc):
        self.val = val #value
        self.lr = lr #left range
        self.rr = rr #right range
        self.lc = lc #left child
        self.rc = rc #right child

def seg_func(a,b): #seg_tree function, edit this according to need
    # example for finding maximum of subarray
    return max(a,b)
    
        
def seg_search(left: int, right: int, node: Tree): #searching function

    if left == node.lr and right == node.rr: return node.val #exact range covered by current node
    if node.lc == None: return seg_search(left,right,node.rc) #special last node case

    """
    current node has two children
    ll -> left child's left range
    lr -> left child's right range
    rl -> right child's left range
    rr -> right child's right range
    lv -> value from left side
    rv -> value from right side
    """
    ll,lr,rl,rr = node.lc.lr,node.lc.rr,node.rc.lr,node.rc.rr
    lv,rv = 0,0 
    if left <= lr: #left child is involved
        if left == ll and right >= lr: #left child is fully in range
            lv = node.lc.val
        else: lv = seg_search(left,min(lr,right),node.lc)
    if right >= rl: #right child is involved
        if right == rr and left <= rl: #right child is fully in range
            rv = node.rc.val
        else: rv = seg_search(max(rl,left),right,node.rc)
    return seg_func(lv,rv)



def create_segtree(ar: list) -> Tree:
    ar_len = len(ar)

    #create a node for each element in the list, this is the bottom layer
    nodes = list()
    for i in range(ar_len):
        tmp = Tree(ar[i],i,i,None,None)
        nodes.append(tmp)

    #create parent nodes of previous layer
    while ar_len != 1:
        layer = list()
        for j in range(ar_len//2):
            left,right = nodes[2*j],nodes[2*j+1] #children of new node
            tmp = Tree(seg_func(left.val,right.val),left.lr,right.rr,left,right)
            layer.append(tmp)
            
        if ar_len % 2 == 1: #odd # of nodes, last node special case
            right = nodes[-1]
            tmp = Tree(right.val,right.lr,right.rr,None,right)
            layer.append(tmp)
            ar_len += 1
            
        #update top layer and ar_len
        ar_len = ar_len // 2
        nodes = layer
    return nodes[0] #only head node left in array

if __name__ == "__main__":
    #example use
    ar = [8,2,9,3,7,4,3,5]
    segtree = create_segtree(ar)
    print("maximum from index 3 to index 6 is:",str(seg_search(3,6,segtree)))
    print("expected value is:",str(max(ar[3:7])))
    


